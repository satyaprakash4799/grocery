from django.urls import path
from .views import user_details,user_profile, create_user, logout

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('', user_details, name='user'),
    path('profile/', user_profile, name='profile'),
    path('logout/', logout, name='logout'),
]
