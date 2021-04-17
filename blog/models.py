from django.db import models
from django.contrib.auth.models import User


# author model
class Author(models.Model):
    author = models.OneToOneField(User, on_delete= models.CASCADE)

    class Meta:
        verbose_name_plural = 'Author'

    def __str__(self):
        return self.author.username


# Catagory model
class Catagory(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Catagory'

    def __str__(self):
        return self.name 

# tags model
class Tag(models.Model):
    name  = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name 

# Blog model 
class Blog(models.Model):
    title  = models.CharField(max_length=200, null=True)
    detail = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='images/media', null=True)
    catagories = models.ManyToManyField(Catagory)
    tags = models.ManyToManyField(Tag, blank=True)
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
        return f" {self.title} | { self.author } "

# email marketing system 
class EmailSignUp(models.Model):
    email  = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = " User Emails"

    def __str__(self):
        return self.email

