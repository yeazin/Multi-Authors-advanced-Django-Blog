from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from blog.models import Blog, Catagory, Tag
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator



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

# login View
class LoginView(View):    
    def get(self,request,*args,**kwargs):
        return render(request,'dashboard/log.html')
    
    def post(self,request,*args,**kwargs):
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
        return render(request,'dashboard/post_listing_active.html',context)

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
        return render(request,'dashboard/post_listing_pending.html',context)     

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