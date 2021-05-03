from django.db import models
from dashboard.models import Author


# Catagory model
class Catagory(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Catagory'

    def __str__(self):
        return str(self.name) 

# tags model
class Tag(models.Model):
    name  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name 

# Blog model 
class Blog(models.Model):
    status = (
        ('active','active'),
        ('pending','pending')
    )
    visibility = (
        ('show','show'),
        ('hide','hide')
    )
    title  = models.CharField(max_length=200, null=True)
    detail = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/media', null=True, blank=True)
    #catagories = models.ManyToManyField(Catagory)
    catagories = models.ForeignKey(Catagory,on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=status, default='pending')
    #show_hide = models.CharField(max_length=5,choices=visibility, default='show')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def overview(self):
        short = self.detail[:30]
        return short 
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url 

    def __str__(self):
        return str(self.title)

# email marketing system 
class EmailSignUp(models.Model):
    email  = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = " User Emails"

    def __str__(self):
        return self.email

# made by Nazrul Islam Yeasin 
# Facebook : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io