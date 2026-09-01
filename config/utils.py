import json


def json_body(request) -> dict:
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return {}
