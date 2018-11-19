from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500, blank=True)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    header = models.CharField(max_length=100)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

