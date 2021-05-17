from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/<int:id>/',views.SingleBlogView.as_view(), name='single_blog' ),
    path('category/<int:id>', views.CatagoryView.as_view(), name='catagory'),
    path('tag/<int:id>', views.TagView.as_view(),name='tag'),
    path('subscribe/', views.SubsCribe.as_view(), name='subscribe'),

    # test
    path('test/', views.test, name='test'),

]