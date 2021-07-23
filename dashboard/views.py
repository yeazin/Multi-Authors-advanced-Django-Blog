from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from blog.models import Blog, Catagory, Tag
from .models import Author
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Count, Sum



# user dashboard views 
class Dashboard(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        user = request.user 
        post = user.author.blog_set.all()
        post_count = post.count()
        post_active = user.author.blog_set.filter(status='active')
        post_active_count = post_active.count()
        post_pending = user.author.blog_set.filter(status='pending')
        post_pending_count = post_pending.count()
        # showing the sum of visit count of spacific users 
        post_visit_count = post.aggregate(Sum('visit_count'))['visit_count__sum']
        context= {
            'user':user,
            'post':post,
            'post_count':post_count,
            'post_active':post_active,
            'post_pending':post_pending,
            'post_active_count':post_active_count,
            'post_pending_count':post_pending_count,
            'count':post_visit_count

        }
        return render(request,'dashboard/dash/dashboard.html',context)

# Create Author 
class CreateAuthor(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request,'dashboard/user/create_user.html')

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            user = User.objects.filter(username=username)
            email_obj = Author.objects.filter(email=email)
            if user:
                messages.warning(request,'Username Already Exits!')
                return redirect ('create_user')
            elif password1 != password2:
                messages.warning(request,'Password Didn`t match')
                return redirect('create_user')
            else:
                auth_info={
                    'username':username,
                    'password':make_password(password1)
                }
                user = User(**auth_info)
                user.save()
            if email_obj:
                messages.warning(request,'Email Already Exits!')
                return redirect('create_user')
            else:
                user_other_obj = Author(author=user, email=email, first_name=first_name, last_name= last_name)
                user_other_obj.save(Author)
                messages.success(request,'Thanks for Joining Please Log in')
                return redirect('login')

# Author Profile
class AuthorProfile(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request):
        author = request.user
        context= {
            'author':author
        } 
        return render(request,'dashboard/user/profile.html', context)

# Edit Author 
class EditAuthor(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        return render(request,'dashboard/user/edit_profile.html')
        
    def post(self, request):
        obj = request.user.author
        obj.author_image = request.POST.get('image')
        obj.first_name = request.POST.get('fname')
        obj.last_name = request.POST.get('lname')
        obj.email = request.POST.get('email')
        # mail_obj = Author.objects.filter(email=obj.email)
        # if mail_obj == obj.email:
        #     messages.success(request,'Your profile has been updated Successfully')
        #     return redirect('profile')
        # elif mail_obj:
        #     messages.warning(request,'sorry Mail already used')
        #     return redirect ('edit')
        # else:
        obj.save()
        #obj = Author.objects.update(first_name=first_name, last_name=last_name)
        messages.success(request,'Your profile has been updated Successfully')
        return redirect('profile')

# login View
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'dashboard/user/login.html')
    def post(self, request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'username or password didn`t match')
            return redirect('login')

# Logout View
class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
# post listing View Active
class PostListingActive(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        user = request.user 
        post_active = user.author.blog_set.filter(status='active').order_by('-id')
        context={
            'post_active':post_active
        }    
        return render(request,'dashboard/post/post_listing_active.html',context)

# post listing View Pending
class PostListingPending(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)   
    
    def get(self,request,*args,**kwargs):
        user = request.user 
        post_pending = user.author.blog_set.filter(status='Pending').order_by('-id')
        context={
            'post_pending':post_pending
        }    
        return render(request,'dashboard/post/post_listing_pending.html',context)     

# Category Views
class CatagoryFunction(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,*args,**kwargs):
        catagory_obj = Catagory.objects.all().order_by('-id')
        context ={
            'catagory':catagory_obj
        }
        return render(request,'dashboard/catagory/catagory.html', context)

# add category
class AddCatagory(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        return render(request,'dashboard/catagory/catagory.html')

    def post(self,request):
        if request.method == 'POST':
            catagory= request.POST.get('catagory')
            cat_obj = Catagory.objects.filter(name=catagory)
            if cat_obj:
                messages.warning(request,'Sorry This category already in Databse')
                return redirect('category')
            else:  
                obj = Catagory.objects.create(name=catagory)
                obj.save()
                messages.success(request,'Category successfully Added')
                return redirect('category')

# Edit Category
class UpdateCategory(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request, id):
        obj = get_object_or_404(Catagory, id=id)
        obj.name = request.POST.get('category')
        obj.save()
        return redirect('category')

# Delete Category
class DeleteCategory(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self, request, id):
        obj = get_object_or_404(Catagory, id=id)
        obj.delete() 
        return redirect('category') 

# Tag functions
class TagFunction(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request):
        tag_obj = Tag.objects.all().order_by('-id')
        context = {
            'tag':tag_obj
        }   
        return render (request,'dashboard/tag/tag.html', context)
        
# add Tags
class AddTag(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        return render(request,'dashboard/tag/tag.html')

    def post(self,request):
        if request.method == 'POST':
            tag= request.POST.get('tag')
            obj = Tag.objects.create(name=tag)
            obj.save()
            return redirect('tag')

# update Tags
class UpdateTag(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self,request, id):
        obj = get_object_or_404(Tag, id=id)
        obj.name = request.POST.get('tag')
        obj.save()
        return redirect('tag')

# Delete Tags
class DeleteTag(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self, request, id):
        obj = get_object_or_404(Tag, id=id)
        obj.delete() 
        return redirect('tag') 

# Post Lists 
# Create Post
class CreatePost(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        category = Catagory.objects.all()
        context = {
            'category': category
        }
        return render(request,'dashboard/post/create_post.html', context)

    def post(self,request):
        author = request.user.author
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        image = request.FILES.get('image')
        #tag = request.POST.get('category')
        #tag_obj = Tag.objects.get(name=tag)
        category = request.POST.get('category')
        cat_obj = Catagory.objects.get(name=category)

        post_obj = Blog(author=author,title=title, detail=detail,image=image,catagories=cat_obj)
        post_obj.save(post_obj)
        messages.success(request,'created Post Successfully')
        return redirect('all_post')

# All Post show
class AllPost(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        user = request.user.author
        post = user.blog_set.all().order_by('-id')
        context = {
            'post':post
        }
        return render(request,'dashboard/post/all_post.html',context)

# Post detail 
class PostView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self, request,id):
        post_obj = get_object_or_404(Blog, id=id)
        context={
            'post':post_obj
        }
        return render(request,'dashboard/post/post_view.html', context)
    
        
# Edit Post
class EditPost(View):
    @method_decorator(login_required(login_url='login'))   
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        obj = get_object_or_404(Blog, id=id)
        cat_obj = Catagory.objects.all()
        context= {
            'obj':obj,
            'cat':cat_obj
        }
        return render(request,'dashboard/post/edit_post.html', context)
    
    def post(self,request,id):
        obj = get_object_or_404(Blog , id=id)
        obj.title = request.POST.get('name')
        obj.title = request.POST.get('title')
        obj.detail = request.POST.get('detail')
        obj.image = request.FILES.get('image')
        category = request.POST.get('category')
        obj.cat_obj = Catagory.objects.get(name=category)
        obj.save()
        messages.success(request,'Post has been Updated')
        return redirect('all_post')

# Make VIsible
class VisiblePost(View):
    @method_decorator(login_required(login_url='login'))   
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id):
        obj  = Blog.objects.get(id=id)
        obj.visible = True
        obj.save()
        messages.success(request,'Post is Visible')
        # Redirect To the Same Page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Make Hidden
class HidePost(View):
    @method_decorator(login_required(login_url='login'))   
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id):
        obj  = Blog.objects.get(id=id)
        obj.visible = False
        obj.save()
        messages.success(request,'Post is Hidden')

        # Redirect To the Same Page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Delete Posts
class DeletePost(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    

    def post(self, request,id):
        obj = get_object_or_404(Blog, id=id)
        obj.delete()
        messages.success(request,'Post Has Been Deleted')
        # Redirect To the Same Page
        return redirect('all_post')

# made by Nazrul Islam Yeasin 
# Facebook : https://facebook.com/yeazin.io
# Twitter : https://twitter.com/_yeazin
# Github : https://github.com/yeazin
# linked In : https://www.linkedin.com/in/yeazin/
# website : yeazin.github.io