from django.contrib import admin
from .models import Free, GameMatch, DailySureTips, OverUnderBet, FreeBet, CorrectScoreBet, MultiBet, Match, HTFTOutcome, FixedVIPBet, FixedMatch, VIP, bestOffers

# Register your models here.
admin.site.register(GameMatch)
admin.site.register(DailySureTips)
admin.site.register(OverUnderBet)
admin.site.register(FreeBet)

admin.site.register(Free)


admin.site.register(CorrectScoreBet)
admin.site.register(MultiBet)
admin.site.register(Match)
admin.site.register(HTFTOutcome)
admin.site.register(FixedVIPBet)
admin.site.register(FixedMatch)

admin.site.register(VIP)


admin.site.register(bestOffers)