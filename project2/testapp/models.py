from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def __str__(self):
        return
