from django.db import models
from django.utils import timezone
# Create your models here.
class BookData(models.Model):
    jyanru = models.CharField(max_length=20)
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    purchase_date = models.DateField(verbose_name='購入日', blank=True, null=True)
    #purchase_date = models.DateField(default=timezone.now)
    
    price = models.IntegerField(default=0)
    memo = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.bookname
