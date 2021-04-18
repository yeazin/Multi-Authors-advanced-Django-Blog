from django.shortcuts import render
from django.views import View
from blog.models import Blog

# user dashboard views 
class Dashboard(View):
    def get(self,request,*args,**kwargs):
        user = request.user 
        post = user.author.blog_set.all()
        post_count = post.count()
        post_active = user.author.blog_set.filter(status='active').count()
        post_pending = user.author.blog_set.filter(status='pending').count()
        context= {
            'user':user,
            'post':post,
            'post_count':post_count,
            'post_active':post_active,
            'post_pending':post_pending

        }
        return render(request,'dashboard/dashboard.html',context)
