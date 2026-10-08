from rest_framework.views import APIView
from plans.service.plan_service import create_plan, get_all_plans, get_plan_by_id, update_plan
from plans.serializer.plan_serializer import PlanSerializer
from accounts.security.permission.preauthorize import preauthorize
from config.api_response import success, error


class PlanView(APIView):

    @preauthorize("CREATE_PLAN")
    def post(self, request):
        try:
            serializer = PlanSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            plan = create_plan(serializer.validated_data)
            return success(data={"plan": plan}, message="Plan created successfully", status_code=201)
        except ValueError as e:
            return error(message=str(e), status_code=409)
        except Exception:
            return error(message="Internal server error", status_code=500)

    def get(self, request):
        try:
            plans = get_all_plans()
            return success(data={"plans": plans}, message="Plans fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)


class PlanDetailView(APIView):

    @preauthorize("GET_PLAN_BY_ID")
    def get(self, request, plan_id):
        try:
            plan = get_plan_by_id(plan_id)
            return success(data={"plan": plan}, message="Plan fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("UPDATE_PLAN")
    def put(self, request, plan_id):
        try:
            serializer = PlanSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            plan = update_plan(plan_id, serializer.validated_data)
            return success(data={"plan": plan}, message="Plan updated successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)
