import logging

from django.http import JsonResponse

logger = logging.getLogger(__name__)


class GlobalExceptionHandler:
    """
    Catches unhandled exceptions globally across all controllers.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            return JsonResponse({"error": str(exception)}, status=400)

        logger.error("Unhandled exception: %s", str(exception), exc_info=True)
        return JsonResponse({"error": "Internal server error"}, status=500)
