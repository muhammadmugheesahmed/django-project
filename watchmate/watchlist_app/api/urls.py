from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate

urlpatterns = [
   
    path("watchlist/",WatchListAV.as_view(),name='watchlist-list'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(),name='watchlist-detail'),
    path("stream/",StreamPlatformAV.as_view(),name='stream-platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),name='stream-platform-detail'),
    
    # path("review/",ReviewList.as_view(),name='Review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(),name='Review-detail'),
    
    path("stream/<int:pk>/review-create/",ReviewCreate.as_view(),name='Review-create'),
    path("stream/<int:pk>/review/",ReviewList.as_view(),name='Review-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(),name='Review-detail'),
    
]
