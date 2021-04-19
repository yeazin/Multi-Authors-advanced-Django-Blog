from django.db import models
from django.contrib.auth.models import User


# author model
class Author(models.Model):
    author = models.OneToOneField(User, on_delete= models.CASCADE)
    designation = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural = 'Author'

    def __str__(self):
        return self.author.username

# made by Nazrul Islam Yeasin 
# Facebook : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io
