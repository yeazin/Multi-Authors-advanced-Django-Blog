# for blog views  global varibale calls
from .models import Catagory, Blog
from  django.db.models import Count

 
# src = https://able.bio/rhett/how-to-order-by-count-of-a-foreignkey-field-in-django--26y1ug1
def globalVariable(request):
    # showing The categories with most post under each category
    category = Catagory.objects.all()\
        .annotate(post_count=Count('blog'))\
        .filter(blog__isnull=False)\
        .order_by('-post_count')[:4]
    category_count = category.count()
    context = {
        'category':category,
        'cat_count':category_count
        }
    return context
    
## Information
#.annotate(post_count=Count('blog'))\ -> countin the blog post under each category
#.filter(blog__isnull=False)\ -> Filtering the blog model so that category without post wont display
#.order_by('-post_count')[:5] -> ordering by most post , category with max posts will show first.