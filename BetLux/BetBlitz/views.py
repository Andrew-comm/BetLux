from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Free, VIP, bestOffers, HTFTOutcome
from .serializers import FreeSerializer, VIPSerializer, BestOffersSerializer, HTFToutcomeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
def homeView(request):    
    response = HttpResponse("This is a simple HTTP response.")
    return response

class freeList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
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
    permission_classes = [IsAuthenticatedOrReadOnly]    
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
    permission_classes = [IsAuthenticatedOrReadOnly]     
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

  #HT_FT  
class HT_FT_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        ht_ft = HTFTOutcome.objects.all()
        serializer = HTFToutcomeSerializer(ht_ft, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HTFToutcomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

