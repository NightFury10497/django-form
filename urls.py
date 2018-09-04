
from django.conf.urls import url
from django.contrib import admin


from justclean import views

urlpatterns = [
#    url(r'^$', views.home , name='home'),
    url(r'^$', views.home , name='home'),
    url(r'^about/', views.about , name='about'),
    url(r'^services/', views.services , name='services'),
    url(r'^contact/', views.contact , name='contact'),
    url(r'^contactpost/', views.contactpost , name='contactpost'),
    url(r'^contactpost2/', views.contactpost2 , name='contactpost2'),
    url(r'^thankyou/', views.thankyou , name='thankyou'),
    url(r'^admin/', admin.site.urls),
]
