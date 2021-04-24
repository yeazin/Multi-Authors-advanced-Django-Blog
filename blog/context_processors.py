# for blog views  global varibale calls
from .models import Blog,Catagory,Tag

def globalVariable(request):
    featured_post = Blog.objects.filter(featured=True, status='active').order_by('-id')
    catagories_obj  = Catagory.objects.all().order_by('-id')
    tags_obj = Tag.objects.all().order_by('-id')
    popular_post = Blog.objects.all().order_by('-id')[:3]
    images_obj = Blog.objects.only('image').order_by('-id')[:6]
    all_post = Blog.objects.all().order_by('-id')
        # pagination Logics
    # paginator = Paginator(all_post, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
            'featured':featured_post,
            'popular': popular_post,
            'catagories':catagories_obj,
            'tags':tags_obj,
            'image':images_obj,
            

        }
    return context
    