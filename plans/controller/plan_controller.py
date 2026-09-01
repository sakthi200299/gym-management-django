from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from plans.dto.plan_request_dto import PlanRequestDTO
from plans.service.plan_service import create_plan, get_all_plans, get_plan_by_id, update_plan
from config.utils import json_body


@method_decorator(csrf_exempt, name="dispatch")
class PlanController(View):

    def post(self, request):
        try:
            dto = PlanRequestDTO(json_body(request))
            plan = create_plan(dto)
            return JsonResponse({"message": "Plan created successfully", "plan": plan}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def get(self, request):
        try:
            plans = get_all_plans()
            return JsonResponse({"plans": plans})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class PlanDetailController(View):

    def get(self, request, plan_id):
        try:
            plan = get_plan_by_id(plan_id)
            return JsonResponse({"plan": plan})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def put(self, request, plan_id):
        try:
            dto = PlanRequestDTO(json_body(request))
            plan = update_plan(plan_id, dto)
            return JsonResponse({"message": "Plan updated successfully", "plan": plan})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)
