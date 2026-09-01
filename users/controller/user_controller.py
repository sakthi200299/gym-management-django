from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from users.dto.user_request_dto import UserRequestDTO
from users.service import user_service
from config.utils import json_body


@method_decorator(csrf_exempt, name="dispatch")
class UserController(View):

    def post(self, request, user_id=None):
        try:
            dto = UserRequestDTO(json_body(request))
            user = user_service.register_user(dto)
            return JsonResponse({"message": "User registered successfully", "user": user}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def get(self, request, user_id=None):
        try:
            if user_id:
                user = user_service.get_user_by_id(user_id)
                return JsonResponse({"user": user})
            users = user_service.get_all_users()
            return JsonResponse({"users": users})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class UserDetailController(View):

    def get(self, request, user_id):
        try:
            user = user_service.get_user_by_id(user_id)
            return JsonResponse({"user": user})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def put(self, request, user_id):
        try:
            dto = UserRequestDTO(json_body(request))
            user = user_service.update_user(user_id, dto)
            return JsonResponse({"message": "User updated successfully", "user": user})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)
