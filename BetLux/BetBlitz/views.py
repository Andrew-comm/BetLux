from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Free, VIP, bestOffers, HTFTOutcome, MultiBet, FixedVIPBet, CorrectScoreBet, DailySureTips, OverUnderBet, GameMatch, FreeBet
from .serializers import FreeSerializer, VIPSerializer, BestOffersSerializer, HTFToutcomeSerializer, multibetSerializer, fixedVIPbetSerializer, correctscoreSerializer, DailySureTipsSerializer, OverUnderBetSerializer, GameMatchSerializer, FreeBetSerializer
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
    

class DailyTipsList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        tips = DailySureTips.objects.all()
        serializer = DailySureTipsSerializer(tips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DailySureTipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OverUnderList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        over_under = OverUnderBet.objects.all()
        serializer = OverUnderBetSerializer(over_under, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OverUnderBetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GameList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        game = GameMatch.objects.all()
        serializer = GameMatchSerializer(game, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BonusList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        bonus = FreeBet.objects.all()
        serializer = FreeBetSerializer(bonus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FreeBetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Multi20_List(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        multi10 = MultiBet.objects.all()
        serializer = multibetSerializer(multi10, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
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
    
    #50+
class Multi50_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        multi50 = MultiBet.objects.all()
        serializer = multibetSerializer(multi50, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    #10+
class Multi10_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        multi10 = MultiBet.objects.all()
        serializer = multibetSerializer(multi10, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    #special
class SpecialVip_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        special = MultiBet.objects.all()
        serializer = multibetSerializer(special, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #fixed VIp
class FixedVip_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        fixed = FixedVIPBet.objects.all()
        serializer = fixedVIPbetSerializer(fixed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = fixedVIPbetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #mixed

class MxedVip_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        mixed = MultiBet.objects.all()
        serializer = multibetSerializer(mixed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#single

class SingleVIP_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        single = MultiBet.objects.all()
        serializer = multibetSerializer(single, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = multibetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    #correct-score

class CorrectScore_list(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]    
    def get(self, request, format=None):
        correct = CorrectScoreBet.objects.all()
        serializer = correctscoreSerializer(correct, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = correctscoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)