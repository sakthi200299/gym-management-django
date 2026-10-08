from rest_framework.views import APIView
from subscriptions.service.subscription_service import create_subscription, get_all_subscriptions, get_subscription_by_id, update_subscription, delete_subscription
from subscriptions.serializer.subscription_serializer import SubscriptionSerializer
from accounts.security.permission.preauthorize import preauthorize
from config.api_response import success, error


class SubscriptionView(APIView):

    @preauthorize("CREATE_SUBSCRIPTION")
    def post(self, request):
        try:
            serializer = SubscriptionSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            sub = create_subscription(serializer.validated_data)
            return success(data={"subscription": sub}, message="Subscription created successfully", status_code=201)
        except ValueError as e:
            return error(message=str(e), status_code=409)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("GET_ALL_SUBSCRIPTIONS")
    def get(self, request):
        try:
            subs = get_all_subscriptions()
            return success(data={"subscriptions": subs}, message="Subscriptions fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)


class SubscriptionDetailView(APIView):

    def get(self, request, sub_id):
        try:
            sub = get_subscription_by_id(sub_id)
            return success(data={"subscription": sub}, message="Subscription fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("UPDATE_SUBSCRIPTION")
    def put(self, request, sub_id):
        try:
            serializer = SubscriptionSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            sub = update_subscription(sub_id, serializer.validated_data)
            return success(data={"subscription": sub}, message="Subscription updated successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("DELETE_SUBSCRIPTION")
    def delete(self, request, sub_id):
        try:
            delete_subscription(sub_id)
            return success(message="Subscription deleted successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)
