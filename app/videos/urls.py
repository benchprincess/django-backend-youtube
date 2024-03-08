from django.urls import path
from . import views
from reactions.views import ReactionDetail

urlpatterns = [
    path('', views.VideoList.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetail.as_view(), name='video-detail'), # api/v1/videos/<int:pk>
    path('<int:video_id>/reaction', ReactionDetail.as_view(), name='video-reaction')
]
