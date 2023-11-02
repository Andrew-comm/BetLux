from django.urls import path
from . views import freeList, VIPList, BestOffersList
urlpatterns = [
    path('free/', freeList.as_view(), name='free'),
    path('VIP',VIPList.as_view(), name='vip' ),
    path('offers',BestOffersList.as_view(), name='offers' )

  
]

