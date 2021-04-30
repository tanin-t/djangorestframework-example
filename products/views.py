from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductCategory, Product
from .serializers import ProductSerializer


class ProductListAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductDetailAPI(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(pk=pk)
            product.name = serializer.validated_data['name']
            product.price = serializer.validated_data['price']
            product.category = serializer.validated_data['category']
            product.save()

            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)
        
