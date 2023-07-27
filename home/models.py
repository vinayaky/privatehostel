from django.db import models

# Create your models here.
class Profile(models.Model):
    image=models.FileField(upload_to='images/',max_length=250,null=True, default=False)
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=200,null=True)
    desc=models.CharField(max_length=600,null=True)
    singles=models.CharField(max_length=100,null=True)
    twos=models.CharField(max_length=100,null=True)
    threes=models.CharField(max_length=100,null=True)
    fours=models.CharField(max_length=100,null=True)
    fours=models.CharField(max_length=100,null=True)
    occupancy=models.CharField(max_length=200,null=True)
    number=models.CharField(max_length=100,null=True)
    uid=models.CharField(max_length=100,null=True)

class onlyimages(models.Model):
     name=models.CharField(max_length=100,null=True)
     image=models.FileField(upload_to='images/',max_length=250,null=True, default=False)
     imagepname=models.CharField(max_length=100,null=True)


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name     
