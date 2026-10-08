from rest_framework.views import APIView
from exercises.service.exercise_service import create_exercise, get_all_exercises, get_exercise_by_id, update_exercise, delete_exercise
from exercises.serializer.exercise_serializer import ExerciseSerializer
from accounts.security.permission.preauthorize import preauthorize
from config.api_response import success, error


class ExerciseView(APIView):

    def post(self, request):
        try:
            serializer = ExerciseSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            exercise = create_exercise(serializer.validated_data)
            return success(data={"exercise": exercise}, message="Exercise created successfully", status_code=201)
        except ValueError as e:
            return error(message=str(e), status_code=409)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("GET_ALL_EXERCISES")
    def get(self, request):
        try:
            exercises = get_all_exercises()
            return success(data={"exercises": exercises}, message="Exercises fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)


class ExerciseDetailView(APIView):

    @preauthorize("GET_EXERCISE_BY_ID")
    def get(self, request, exercise_id):
        try:
            exercise = get_exercise_by_id(exercise_id)
            return success(data={"exercise": exercise}, message="Exercise fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("UPDATE_EXERCISE")
    def put(self, request, exercise_id):
        try:
            serializer = ExerciseSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            exercise = update_exercise(exercise_id, serializer.validated_data)
            return success(data={"exercise": exercise}, message="Exercise updated successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("DELETE_EXERCISE")
    def delete(self, request, exercise_id):
        try:
            delete_exercise(exercise_id)
            return success(message="Exercise deleted successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)
