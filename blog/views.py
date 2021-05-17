from django import views
from django.http import HttpResponseRedirect
from django.db.models.fields import EmailField
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Blog, Catagory,Tag, EmailSignUp
from django.core.paginator import Paginator


class HomeView(View):
    def get(self,request,*args,**kwargs):
        '''
        # featured_post = Blog.objects.filter(featured=True, status='active',show_hide='show').order_by('-id')
        # catagories_obj  = Catagory.objects.all().order_by('-id')
        # tags_obj = Tag.objects.all().order_by('-id')
        # blog_post  = Blog.objects.filter(status='active',show_hide='show').order_by('-id')
        # popular_post = blog_post[:3]
        # images_obj = blog_post.only('image').order_by('-id')[:6]
        # #all_post = Blog.objects.all().order_by('-id')
        # # pagination Logics
        # paginator = Paginator(all_post, 4)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        # context = {
        #     'featured':featured_post,
        #     'popular': popular_post,
        #     'catagories':catagories_obj,
        #     'tags':tags_obj,
        #     'image':images_obj,
        #     'post':page_obj

        # }
        '''
        featured_obj = Blog.objects.all().filter(status='active', visible=True, featured=True).order_by('catagories','-created_at')[:5]
        first_post = featured_obj.first()
        s_post = featured_obj[1]
        last_post = featured_obj[2:]
        post_obj = Blog.objects.all().filter(status='active', visible=True).order_by('catagories','-created_at')
        context={
            'post':post_obj,
            'f_post':featured_obj,
            'first':first_post,
            's_post':s_post,
            'last_post':last_post
            
        }
        return render(request, 'home/index.html',context)

# single blog views
class SingleBlogView(View):
    def get(self,request,id,*args,**kwargs):
        post_obj = get_object_or_404(Blog, id=id)
        post_obj.visit_count = post_obj.visit_count + 1
        post_obj.save()
        releted_post = Blog.objects.filter(author=post_obj.author).exclude(id=id).order_by('-id')[:4]
        # As per templates views 
        first_post = releted_post.first()
        last_post  = releted_post[1:]
        

        context ={
            'post':post_obj,
            'r_post':releted_post,
            'first':first_post,
            'last':last_post
        }
        return render(request,'blogs/post/single_blog.html', context)

# Catagory View
class CatagoryView(View):
    def get(self,request,id,*args,**kwargs):
        catagory_obj = get_object_or_404(Catagory, id=id)
        post = catagory_obj.blog_set.all().order_by('-id')
        context ={
            'catagory':catagory_obj,
            'post':post
        }
        return render(request,'home/category.html', context )

# tag View
class TagView(View):
    def get(self,request,id,*args,**kwargs):
        tag_obj = get_object_or_404(Tag, id=id)
        post = tag_obj.blog_set.all().order_by('-id')
        tag_count = post.count()
        context={
            'tag':tag_obj,
            'post':post,
            'tag_count':tag_count
        }
        return render(request,'home/tag.html',context)


class SubsCribe(View):
    def post(self, request,*args,**kwargs):
        sub_obj = request.POST.get('subscribe')
        subscribe = EmailSignUp.objects.create(email=sub_obj)
        subscribe.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





# made by Nazrul Islam Yeasin 
# Facebook : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io