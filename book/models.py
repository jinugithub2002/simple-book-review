from django.db import models

# Create your models here.
class tbl_book(models.Model):
    title=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=200,null=True)
    genre=models.CharField(max_length=200,null=True)
    price=models.IntegerField(null=True)
    published_date=models.DateField(null=True)
    
class customer_reg(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    number=models.IntegerField(null=True)
    password=models.CharField(max_length=200,null=True)
    
class tbl_review(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    rating=models.CharField(max_length=100,null=True)
    review=models.CharField( max_length=100,null=True)
    book=models.ForeignKey(tbl_book, null=True,on_delete=models.CASCADE)
    
class tbl_cart(models.Model):
    book=models.ForeignKey(tbl_book, null=True,on_delete=models.CASCADE)
    sessions_key=models.CharField(null=True, max_length=100)
    
class tbl_billing(models.Model):
    full_name = models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zip_code=models.IntegerField(null=True)
    