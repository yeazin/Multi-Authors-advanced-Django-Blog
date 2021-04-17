from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Blog, Catagory,Tag, EmailSignUp
from django.core.paginator import Paginator


class HomeView(View):
    def get(self,request,*args,**kwargs):
        featured_post = Blog.objects.filter(featured=True).order_by('-id')
        catagories_obj  = Catagory.objects.all().order_by('-id')
        tags_obj = Tag.objects.all().order_by('-id')
        popular_post = Blog.objects.all().order_by('-id')[:3]
        images_obj = Blog.objects.only('image').order_by('-id')[:6]
        all_post = Blog.objects.all().order_by('-id')
        # pagination Logics
        paginator = Paginator(all_post, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'featured':featured_post,
            'popular': popular_post,
            'catagories':catagories_obj,
            'tags':tags_obj,
            'image':images_obj,
            'post':page_obj

        }
        return render(request, 'home/index.html', context)

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            email_obj = request.POST.get('email')
            email = EmailSignUp(email=email_obj)
            email.save()
            return redirect('home')

# single blog views
class SingleBlogView(View):
    def get(self,request,id,*args,**kwargs):
        post_obj = get_object_or_404(Blog, id=id)
        #releted_post = Blog.objects.filter(catagories=post_obj.catagories).exclude(id=id)

        context ={
            'post':post_obj,
            #'r_post':releted_post
        }
        return render(request,'blogs/single_blog.html', context)





