"""
URL configuration for BetLux project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BetBlitz. views import freeList, VIPList, BestOffersList, HT_FT_list, Multi50_list, Multi10_list, SpecialVip_list, FixedVip_list,MxedVip_list, SingleVIP_list, CorrectScore_list, DailyTipsList, OverUnderList, GameList, BonusList, Multi20_List
from BetBlitz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeView, name='home'), 
    path('free/', freeList.as_view(), name='free'),
    path('VIP/', VIPList.as_view(), name='vip'),     
    path('offers/', BestOffersList.as_view(), name='offers'), 

    path('tips/', DailyTipsList.as_view(), name='tips'), 
    path('over_under/', OverUnderList.as_view(), name='over_under'), 
    path('game/', GameList.as_view(), name='game'), 
    path('bonus/', BonusList.as_view(), name='bonus'), 
    path('multi20/', Multi20_List.as_view(), name='multi20'), 

    path('ht-ft/', HT_FT_list.as_view(), name='ht-ft'),
    path('multi50/', Multi50_list.as_view(), name='multi50'),
    path('multi10/', Multi10_list.as_view(), name='multi10'),
    path('special/', SpecialVip_list.as_view(), name='special'),
    path('fixed-vip/', FixedVip_list.as_view(), name='fixed-vip'),
    path('mixed-vip/', MxedVip_list.as_view(), name='mixed-vip'),
    path('single-vip/', SingleVIP_list.as_view(), name='single-vip'),
    path('correct-score/', CorrectScore_list.as_view(), name='correct-score'),


]

