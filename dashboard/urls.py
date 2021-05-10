from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    # Post 
    path('create-post/',views.CreatePost.as_view(), name="create_post"),
    path('post/', views.AllPost.as_view(), name='all_post'),
    path('post/view/<str:id>', views.PostView.as_view(), name='post'),
    path('post/edit/<str:id>/', views.EditPost.as_view(), name='edit_post'),
    path('post/delete/<str:id>/', views.DeletePost.as_view(), name="delete_post"),
    path('post_listing_active/',views.PostListingActive.as_view(), name='post_listing_active'),
    path('post_listing_pending/', views.PostListingPending.as_view(), name='post_listing_pending'),
    path('visible/post/<str:id>', views.VisiblePost.as_view(), name='visible'),
    path('hidden/post/<str:id>', views.HidePost.as_view(),name='hidden'),
    # Author
    path('profile/',views.AuthorProfile.as_view(), name='profile'),
    path('profile/edit/', views.EditAuthor.as_view(), name="edit"),
    #path('update-author/<str:id>', views.EditAuthor.as_view(), name='update_author' ),
    # category
    path('category/', views.CatagoryFunction.as_view(), name='category'),
    path('add-category/', views.AddCatagory.as_view(), name='add_category'),
    path('edit-category/<str:id>/', views.UpdateCategory.as_view(), name='update_category'),
    path('delete-category/<str:id>', views.DeleteCategory.as_view(), name='delete_category'),
    # tag
    path('tag/', views.AddTag.as_view(), name='tag'),
    path('add-tag/', views.AddTag.as_view(), name='add_tag'),
    path('update-tag/', views.UpdateTag.as_view(), name='update_tag'),
    path('delete-tag/', views.DeleteTag.as_view(), name='delete_tag'),
    
]