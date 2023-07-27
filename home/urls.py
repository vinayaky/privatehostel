from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('profile',views.upload,name='profile'),
    path('about',views.about,name='about'),
    path('contactUs',views.contactUs,name='contactUs'),
    path('login',views.loginpage,name='login'),
    path('signup',views.SignupPage,name='signup'),
    path('logout',views.Logout,name='logout'),
    path('detail/<pid>/<pid2>',views.detail,name='detail'),
    path('upload',views.upload,name='upload'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
