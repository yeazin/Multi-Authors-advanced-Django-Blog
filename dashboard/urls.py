from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('post_listing_active/',views.PostListingActive.as_view(), name='post_listing_active'),
    path('post_listing_pending/', views.PostListingPending.as_view(), name='post_listing_pending'),
    
]