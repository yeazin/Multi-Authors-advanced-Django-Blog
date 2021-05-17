# for blog views  global varibale calls
from .models import Catagory, Blog
from  django.db.models import Count

 
# src = https://able.bio/rhett/how-to-order-by-count-of-a-foreignkey-field-in-django--26y1ug1
def globalVariable(request):
    # showing The categories with most post under each category
    category = Catagory.objects.all()\
        .annotate(post_count=Count('blog'))\
        .order_by('-post_count')[:5]
    context = {
        'category':category
        }
    return context
    