from django.shortcuts import render,redirect,get_object_or_404
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
        context= {
            'user':user,
            'post':post,
            'post_count':post_count,
            'post_active':post_active,
            'post_pending':post_pending,
            'post_active_count':post_active_count,
            'post_pending_count':post_pending_count

        }
        return render(request,'dashboard/dashboard.html',context)

# Create Author 
class CreateAuthor(View):
    def get(self,request,*args,**kwargs):
        return render(request,'dashboard/user/create_user.html')

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
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
                user_other_obj = Author(author=user, email=email)
                user_other_obj.save(Author)
                messages.success(request,'Thanks for Joining Please Log in')
                return redirect('login')

# login View
class LoginView(View):    
    def get(self,request,*args,**kwargs):
        return render(request,'dashboard/user/login.html')
    
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('dashboard')
                else:
                    return ('login') 

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

    def get(self, request):
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



# made by Nazrul Islam Yeasin 
# Facebook : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io