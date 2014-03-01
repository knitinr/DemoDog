from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=80)
    body=models.TextField()
    pubdate=models.DateTimeField(auto_now=True)
    #pubdate=models.DateTimeField() #auto_now=True)