from django.contrib import admin
from .models import Author, Catagory, Blog, Tag, EmailSignUp

admin.site.register(Author)
admin.site.register(Catagory)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(EmailSignUp)
