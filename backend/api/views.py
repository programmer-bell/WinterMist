import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(['GET'])
def all_api(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data,many=True)
    return Response(serializer.data)


# @csrf_exempt
# @api_view(['GET','POST'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
        # Manually process
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] =  model_data.price
        # By using django forms
        # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
        # return JsonResponse(data)


# @api_view(['GET','POST'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):

    if request.method == "GET":
        instance = Product.objects.order_by("?").first()
        data = ProductSerializer(instance).data
        return Response(data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            data = serializer.data
            return Response(data)
        return Response(serializer.errors, status=400)
