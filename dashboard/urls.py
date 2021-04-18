from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('post_listing/',views.PostListing.as_view(), name='post_listing')
    
]