from django.urls import path
from .views import user_details,user_profile

urlpatterns = [
    path('<int:user_id>', user_details, name='user'),
    path('profile/<int:user_id>', user_profile, name='profile')
]
