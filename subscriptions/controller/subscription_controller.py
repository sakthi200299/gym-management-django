from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from subscriptions.dto.subscription_request_dto import SubscriptionRequestDTO
from subscriptions.service.subscription_service import create_subscription, get_all_subscriptions, get_subscription_by_id, update_subscription
from config.utils import json_body


@method_decorator(csrf_exempt, name="dispatch")
class SubscriptionController(View):

    def post(self, request):
        try:
            dto = SubscriptionRequestDTO(json_body(request))
            sub = create_subscription(dto)
            return JsonResponse({"message": "Subscription created successfully", "subscription": sub}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def get(self, request):
        try:
            subs = get_all_subscriptions()
            return JsonResponse({"subscriptions": subs})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class SubscriptionDetailController(View):

    def get(self, request, sub_id):
        try:
            sub = get_subscription_by_id(sub_id)
            return JsonResponse({"subscription": sub})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def put(self, request, sub_id):
        try:
            dto = SubscriptionRequestDTO(json_body(request))
            sub = update_subscription(sub_id, dto)
            return JsonResponse({"message": "Subscription updated successfully", "subscription": sub})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)
