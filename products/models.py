from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length = 250)
    pubdate = models.DateTimeField()
    body= models.TextField()
    url= models.TextField()
    icon = models.ImageField(upload_to = 'images/')
    image = models.ImageField(upload_to = 'images/')
    votes_total = models.IntegerField(default = 1)
    hunter = models.ForeignKey(User , on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title

     