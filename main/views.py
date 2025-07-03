from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json

@csrf_exempt
def main(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name", '')
        email = data.get("email", "")
        phone = data.get("phone", "")
        city = data.get("city", "")

        return JsonResponse(
            {
                'status': True,
                'message': 'Заявка отправлено!'
            }
        )
    return JsonResponse(
        {
            'status': False,
            'message': 'Разрешается только POST запрос'
        }
    )