from django.shortcuts import render
from django.views import View
from blog.models import Blog

# user dashboard views 
class Dashboard(View):
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
