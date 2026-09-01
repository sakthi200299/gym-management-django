from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from exercises.dto.exercise_request_dto import ExerciseRequestDTO
from exercises.service.exercise_service import create_exercise, get_all_exercises, get_exercise_by_id, update_exercise
from config.utils import json_body


@method_decorator(csrf_exempt, name="dispatch")
class ExerciseController(View):

    def post(self, request):
        try:
            dto = ExerciseRequestDTO(json_body(request))
            exercise = create_exercise(dto)
            return JsonResponse({"message": "Exercise created successfully", "exercise": exercise}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def get(self, request):
        try:
            exercises = get_all_exercises()
            return JsonResponse({"exercises": exercises})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class ExerciseDetailController(View):

    def get(self, request, exercise_id):
        try:
            exercise = get_exercise_by_id(exercise_id)
            return JsonResponse({"exercise": exercise})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def put(self, request, exercise_id):
        try:
            dto = ExerciseRequestDTO(json_body(request))
            exercise = update_exercise(exercise_id, dto)
            return JsonResponse({"message": "Exercise updated successfully", "exercise": exercise})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)
