from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/<int:id>/',views.SingleBlogView.as_view(), name='single_blog' ),
    path('catagory/<int:id>', views.CatagoryView.as_view(), name='catagory')
]