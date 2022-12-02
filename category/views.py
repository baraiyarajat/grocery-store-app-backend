from .models import Category
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from django.http.response import JsonResponse


@api_view(['GET', ])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(category_serializer.data, safe=False)


@api_view(['GET', ])
def category_details(request, category_id):
    if request.method == 'GET':
        category = Category.objects.get(id=category_id)

        category_serializer = CategorySerializer(category)
        return JsonResponse(category_serializer.data, safe=False)


@api_view(['GET', ])
def category_details_by_slug(request, category_slug):
    if request.method == 'GET':
        category = Category.objects.get(slug=category_slug)

        category_serializer = CategorySerializer(category)
        return JsonResponse(category_serializer.data, safe=False)
