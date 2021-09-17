from django.urls import path
from .views.profile_views import Profiles, ProfileDetail
from .views.likes_views import Like, LikeDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('profiles/', Profiles.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('userprofile/', Profiles.as_view(), name='userprofile'),
    path('likes/', Like.as_view(), name='likes'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
