from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('post_listing_active/',views.PostListingActive.as_view(), name='post_listing_active'),
    path('post_listing_pending/', views.PostListingPending.as_view(), name='post_listing_pending'),
    # category
    path('category/', views.CatagoryFunction.as_view(), name='category'),
    path('edit-category/<str:id>/', views.UpdateCategory.as_view(), name='update_category'),
    path('delete-category/<str:id>', views.DeleteCategory.as_view(), name='delete_category')
    
]