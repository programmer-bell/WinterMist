import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.forms.models import model_to_dict

@csrf_exempt
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # Manually process
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] =  model_data.price

        # By using django forms
        data = model_to_dict(model_data,fields=['id','title','price'])
    return JsonResponse(data)
