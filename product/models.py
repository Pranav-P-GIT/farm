from django.db import models

# Create your models here.
from home.models import FarmProduct

class comment(models.Model):
    pro=models.ForeignKey(FarmProduct,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    cmnt=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    