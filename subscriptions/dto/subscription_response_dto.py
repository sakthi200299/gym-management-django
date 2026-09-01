class SubscriptionResponseDTO:

    def __init__(self, id, status, start_date, end_date, user: dict, plan: dict):
        self.id = id
        self.status = status
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.user = user
        self.plan = plan

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "status": self.status,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "user": self.user,
            "plan": self.plan,
        }
