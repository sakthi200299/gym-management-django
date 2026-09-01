from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from trainers.dto.trainer_request_dto import TrainerRequestDTO
from trainers.service.trainer_service import create_trainer, get_all_trainers, get_trainer_by_id, update_trainer
from config.utils import json_body


@method_decorator(csrf_exempt, name="dispatch")
class TrainerController(View):

    def post(self, request):
        try:
            dto = TrainerRequestDTO(json_body(request))
            trainer = create_trainer(dto)
            return JsonResponse({"message": "Trainer created successfully", "trainer": trainer}, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=409)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def get(self, request):
        try:
            trainers = get_all_trainers()
            return JsonResponse({"trainers": trainers})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)


@method_decorator(csrf_exempt, name="dispatch")
class TrainerDetailController(View):

    def get(self, request, trainer_id):
        try:
            trainer = get_trainer_by_id(trainer_id)
            return JsonResponse({"trainer": trainer})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)

    def put(self, request, trainer_id):
        try:
            dto = TrainerRequestDTO(json_body(request))
            trainer = update_trainer(trainer_id, dto)
            return JsonResponse({"message": "Trainer updated successfully", "trainer": trainer})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Internal server error"}, status=500)
