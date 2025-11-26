# api/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print('The get method:',request.GET) # url query params
    print('The post method:',request.POST) # url query params
    print("Raw body:", body)
    print("Parsed JSON:", data)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
