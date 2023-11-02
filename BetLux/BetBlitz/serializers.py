from rest_framework import serializers

from .models import Free, VIP, bestOffers, GameMatch, DailySureTips, OverUnderBet, FreeBet, CorrectScoreBet, MultiBet, Match, HTFTOutcome, FixedVIPBet, FixedMatch


#serializer for Free
class GameMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMatch
        fields = '__all__'  

class DailySureTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySureTips
        fields = '__all__'

class OverUnderBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverUnderBet
        fields = '__all__'

class FreeBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBet
        fields = '__all__'

class FreeSerializer(serializers.ModelSerializer):
    daily_sure_tips = DailySureTipsSerializer()
    over_under = OverUnderBetSerializer()
    Basketball = GameMatchSerializer()
    FootballTips = DailySureTipsSerializer()
    single_tips = DailySureTipsSerializer()
    bonus_surprise = FreeBetSerializer()
    Tennis = GameMatchSerializer()

    class Meta:
        model = Free
        fields = '__all__'

  



#serializer for VIP

class correctscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectScoreBet
        fields = '__all__'


class multibetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiBet
        fields = '__all__'

class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class HTFToutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTFTOutcome
        fields = '__all__'
        
class fixedVIPbetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedVIPBet
        fields = '__all__'


class fixedmatchSerializer(serializers.ModelSerializer):
    class Meta:
        models = FixedMatch
        fields = '__all__'




class VIPSerializer(serializers.ModelSerializer):
    correct_score = correctscoreSerializer()
    multi_50_plus_odd_vip = multibetSerializer()
    special_vip = multibetSerializer()
    mixed_vip = multibetSerializer()
    HT_FT_Tip = HTFToutcomeSerializer()
    multi_10_plus_odd_vip = multibetSerializer()
    fixed_vip = fixedVIPbetSerializer()
    single_vip = fixedVIPbetSerializer()

    class Meta:

        model = VIP
        fields = '__all__'


class BestOffersSerializer(serializers.ModelSerializer):
    starter_vip = fixedVIPbetSerializer()
    premium_vip = fixedVIPbetSerializer()

    class Meta:
        model = bestOffers
        fields = '__all__'
