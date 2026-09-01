from subscriptions.dto.subscription_request_dto import SubscriptionRequestDTO
from subscriptions.dto.subscription_response_dto import SubscriptionResponseDTO
from subscriptions.model.subscription import Subscription


class SubscriptionMapper:

    @staticmethod
    def to_entity(dto: SubscriptionRequestDTO) -> dict:
        return {
            "start_date": dto.start_date,
            "end_date": dto.end_date,
            "status": dto.status,
        }

    @staticmethod
    def to_response_dto(sub: Subscription) -> SubscriptionResponseDTO:
        return SubscriptionResponseDTO(
            id=sub.id,
            status=sub.status,
            start_date=sub.start_date,
            end_date=sub.end_date,
            user={"id": sub.user.id, "name": sub.user.name, "email": sub.user.email},
            plan={"id": sub.plan.id, "name": sub.plan.name, "price": str(sub.plan.price)},
        )

    @staticmethod
    def to_response_dto_list(subs: list) -> list:
        return [SubscriptionMapper.to_response_dto(s).to_dict() for s in subs]
