from django.db import models

# 1 free

# This is model for basketball and tennis
class GameMatch(models.Model):
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    odds_home_team = models.DecimalField(max_digits=5, decimal_places=2)
    odds_away_team = models.DecimalField(max_digits=5, decimal_places=2)
    

    def __str__(self):
        return f"{self.home_team} vs. {self.away_team} - {self.date}"
    

class DailySureTips(models.Model):
    date = models.DateField()
    sport = models.CharField(max_length=50)
    matches = models.TextField()
    prediction = models.TextField()
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    provider = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sport} - {self.date}"

    class Meta:
        verbose_name_plural = "Daily Sure Tips"

#over/under
class OverUnderBet(models.Model):    
    game = models.CharField(max_length=100, help_text="Name of the game or event")
    total_value = models.DecimalField(max_digits=5, decimal_places=2, help_text="The predefined total value")
    bet_type = models.CharField(max_length=10, choices=[("Over", "Over"), ("Under", "Under")], help_text="Bet type (Over or Under)")

    def __str__(self):
        return f"{self.game} - {self.bet_type} - Total: {self.total_value}"

    class Meta:
        verbose_name_plural = "Over/Under Bets"



class FreeBet(models.Model):
    
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()
    
    def __str__(self):
        return f"Free Bet for ${self.amount}"
    


    


class Free(models.Model):
    daily_sure_tips = models.ForeignKey(DailySureTips, on_delete=models.PROTECT, null=True, blank=True, related_name='daily_sure_tips')
    over_under =  models.ForeignKey(OverUnderBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='over_under')
    Basketball = models.ForeignKey(GameMatch, on_delete=models.SET_NULL, null=True, blank=True, related_name='basketball')
    FootballTips = models.ForeignKey(DailySureTips, on_delete=models.PROTECT, null=True, blank=True, related_name='football_tips_free')
    single_tips = models.ForeignKey(DailySureTips, on_delete=models.PROTECT, null=True, blank=True, related_name='single_tips_free')
    bonus_surprise = models.ForeignKey(FreeBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='bonus_surprise_free')
    Tennis = models.ForeignKey(GameMatch, on_delete=models.SET_NULL, null=True, blank=True, related_name='tennis_free')
    daily20 = models.ForeignKey('MultiBet', on_delete=models.SET_NULL, null =True, blank=True)




#2 for VIP

#correct score
class CorrectScoreBet(models.Model):    
    match = models.CharField(max_length=100)  
    team_a = models.CharField(max_length=50)
    team_b = models.CharField(max_length=50)   
    exact_score = models.CharField(max_length=10)  
    odds = models.DecimalField(max_digits=5, decimal_places=2)  


    def __str__(self):
        return self.match 
    

#multibets
class MultiBet(models.Model):    
    bettor = models.CharField(max_length=100)    
    matches = models.ManyToManyField('Match', related_name='multi_bets')    
    total_odds = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)    
     
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Calculate the total odds by multiplying the odds of selected matches
        if not self.total_odds:
            self.total_odds = 1  # Initialize total odds to 1
            for match in self.matches.all():
                self.total_odds *= match.odds
        super(MultiBet, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.bettor}'s MultiBet - Total Odds: {self.total_odds}"

class Match(models.Model):    
    match_name = models.CharField(max_length=100)    
    odds = models.DecimalField(max_digits=8, decimal_places=2)  
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.match_name
    

    #ht-ft oucomes
class HTFTOutcome(models.Model):
    outcome_choices = [
        ('HH', 'Home team wins in first half and full-time'),
        ('HD', 'Home team wins in first half, match ends in draw'),
        ('HA', 'Home team wins in first half, away team wins at full-time'),
        ('DH', 'Draw in first half, home team wins at full-time'),
        ('DD', 'Draw in first half and full-time'),
        ('DA', 'Draw in first half, away team wins at full-time'),
        ('AH', 'Away team wins in first half, home team wins at full-time'),
        ('AD', 'Away team wins in first half, match ends in draw'),
        ('AA', 'Away team wins in first half and full-time'),
    ]

    outcome = models.CharField(
        max_length=2,
        choices=outcome_choices,
        unique=True,
    )

    def __str__(self):
        return self.get_outcome_display()
    

#fixed-vip

class FixedVIPBet(models.Model):
    match = models.ForeignKey('FixedMatch', on_delete=models.CASCADE, null =True, blank=True)
    prediction = models.CharField(max_length=255)
    odds = models.DecimalField(max_digits=5, decimal_places=2)
    

    def __str__(self):
        return f"{self.match} - {self.prediction} - Odds: {self.odds}"


class FixedMatch(models.Model):
    date = models.DateField()
    teams = models.CharField(max_length=255)
    sport = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.teams} - {self.date}"


#2 VIP
class VIP(models.Model):
    correct_score =  models.ForeignKey(CorrectScoreBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='correct_score_vip')
    multi_50_plus_odd_vip = models.ForeignKey(MultiBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_50_plus_odd_vip')
    special_vip = models.ForeignKey(MultiBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='special_vip')
    mixed_vip = models.ForeignKey(MultiBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='mixed_vip')
    HT_FT_Tip  =  models.ForeignKey(HTFTOutcome, on_delete=models.SET_NULL, null=True, blank=True, related_name='ht_ft_tip_vip')
    multi_10_plus_odd_vip = models.ForeignKey(MultiBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_10_plus_odd_vip')
    fixed_vip = models.ForeignKey(FixedVIPBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='fixed_vip')
    single_vip = models.ForeignKey(FixedVIPBet, on_delete=models.SET_NULL, null=True, blank=True, related_name='single_vip')



class bestOffers(models.Model):
    starter_vip = models.ForeignKey(FixedVIPBet, on_delete=models.SET_NULL,null=True, blank=True)
    premium_vip = models.ForeignKey(FixedVIPBet, on_delete=models.SET_NULL,null=True, blank=True, related_name='premium_vip')
