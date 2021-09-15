from django.urls import path
from .views.profile_views import Profiles, ProfileDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('profiles/', Profiles.as_view(), name='mangos'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
