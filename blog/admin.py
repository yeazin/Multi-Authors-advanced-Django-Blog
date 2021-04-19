from django.contrib import admin
from .models import Author, Catagory, Blog, Tag, EmailSignUp


admin.site.register(Catagory)
class BlogAdmin(admin.ModelAdmin):
    class Meta:
        list_display=('author','title','status','created_at','featured')
        ordering = ['-created_at']
        search_fields = ('name','email')
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(EmailSignUp)

# made by Nazrul Islam Yeasin 
# Facebbok : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io
