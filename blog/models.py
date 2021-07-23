
import uuid
from django.db import models
from dashboard.models import Author


# Catagory model
class Catagory(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    image = models.CharField(max_length=300, null=True, blank=True )
    description = models.CharField(max_length=500, null=True,blank=True, verbose_name='Description')

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
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
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
        return f"{ self.title} | { self.author.author.username} | { self.catagories} | { self.status}"

# Comment Class
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} | {self.name } "

# Reply Class
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='reply')
    name = models.CharField(max_length=200, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} | { self.name } |{ self.created_at }"


# email marketing system 
class EmailSignUp(models.Model):
    email  = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = " User Emails"

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Name')
    email = models.EmailField(null=True)
    messages = models.TextField()
    subject = models.CharField(max_length=200, null=True, verbose_name='Subjects' )

    def __str__(self):
        return f"{ self.name } | { self.subject}" 


# made by Nazrul Islam Yeasin 
# Facebook : https://facebook.com/yeazin.io
# Twitter : https://twitter.com/_yeazin
# Github : https://github.com/yeazin
# linked In : https://www.linkedin.com/in/yeazin/
# website : yeazin.github.io