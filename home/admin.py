from django.contrib import admin
from django.contrib.admin.sites import site
from home.models import Profile,onlyimages,Contact
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display=('occupancy','uid','image','number','name','address','desc','singles','twos','threes','fours')


class image(admin.ModelAdmin):
    list_display=('name','image','imagepname')


class feed(admin.ModelAdmin):
    list_display=('name','email','phone','date','desc')

   

admin.site.register(onlyimages,image) 

admin.site.register(Profile,ImageAdmin)  

admin.site.register(Contact,feed)
