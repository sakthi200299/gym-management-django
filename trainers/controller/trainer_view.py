from rest_framework.views import APIView
from trainers.service.trainer_service import create_trainer, get_all_trainers, get_trainer_by_id, update_trainer
from trainers.serializer.trainer_serializer import TrainerSerializer
from accounts.security.permission.preauthorize import preauthorize
from config.api_response import success, error


class TrainerView(APIView):

    @preauthorize("CREATE_TRAINER")
    def post(self, request):
        try:
            serializer = TrainerSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            trainer = create_trainer(serializer.validated_data)
            return success(data={"trainer": trainer}, message="Trainer created successfully", status_code=201)
        except ValueError as e:
            return error(message=str(e), status_code=409)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("GET_ALL_TRAINERS")
    def get(self, request):
        try:
            trainers = get_all_trainers()
            return success(data={"trainers": trainers}, message="Trainers fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)


class TrainerDetailView(APIView):

    @preauthorize("GET_TRAINER_BY_ID")
    def get(self, request, trainer_id):
        try:
            trainer = get_trainer_by_id(trainer_id)
            return success(data={"trainer": trainer}, message="Trainer fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("UPDATE_TRAINER")
    def put(self, request, trainer_id):
        try:
            serializer = TrainerSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            trainer = update_trainer(trainer_id, serializer.validated_data)
            return success(data={"trainer": trainer}, message="Trainer updated successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)
