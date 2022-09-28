from django.urls import path
from .views import create_user, logout, UserDetailsView, UserProfilesView,AddressView, AddressDetailsView

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('', UserDetailsView.as_view(), name='user'),
    path('profile/', UserProfilesView.as_view(), name='profile'),
    path('address/', AddressView.as_view(), name='address'),
    path('address/<int:pk>/', AddressDetailsView.as_view(), name='address_details'),
    path('logout/', logout, name='logout'),
]
