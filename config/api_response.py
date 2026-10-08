from django.http import JsonResponse


def success(data=None, message="Success", status_code=200) -> JsonResponse:
    return JsonResponse({
        "status_code": status_code,
        "status": "success",
        "message": message,
        "data": data,
    }, status=status_code)


def error(message="Error", status_code=400) -> JsonResponse:
    return JsonResponse({
        "status_code": status_code,
        "status": "error",
        "message": message,
        "data": None,
    }, status=status_code)
