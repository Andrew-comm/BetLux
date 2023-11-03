from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Free, VIP, bestOffers
from .serializers import FreeSerializer, VIPSerializer, BestOffersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
def homeView(request):    
    response = HttpResponse("This is a simple HTTP response.")
    return response

class freeList(APIView):    
    def get(self, request, format=None):
        free = Free.objects.all()
        serializer = FreeSerializer(free, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VIPList(APIView):    
    def get(self, request, format=None):
        vip = VIP.objects.all()
        serializer = VIPSerializer(vip, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VIPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BestOffersList(APIView):    
    def get(self, request, format=None):
        offers = bestOffers.objects.all()
        serializer = BestOffersSerializer(offers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BestOffersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def free_list(request,format=None):
#     if request.method == 'GET':
#         free = Free.objects.all()
#         serializer = FreeSerializer(free, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         serializer = FreeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def drink_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         free = Free.objects.get(pk=pk)
#     except Free.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = FreeSerializer(free)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = FreeSerializer(free, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         free.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)