from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField





class Blog(models.Model):
    name = models.CharField(max_length = 100,default="")
    title = models.CharField(max_length = 100,default="")
    id = models.AutoField(primary_key=True)
    short_desc = models.CharField(max_length = 200,default="")
    content = RichTextField()
    thumbnail = models.ImageField(upload_to = "blogimages")
    created_at = models.TimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    name = models.CharField(max_length=100,default="")
    blogparent = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Reply(models.Model):
    name = models.CharField(max_length=100,default="")
    commentparent = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name