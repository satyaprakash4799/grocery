from django.urls import path
from .views import user_profile, create_user, logout, UserDetailsView, UserProfilesView

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('', UserDetailsView.as_view(), name='user'),
    path('profile/', UserProfilesView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]
