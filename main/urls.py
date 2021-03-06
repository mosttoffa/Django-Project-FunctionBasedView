from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^panel/$', views.panel, name='panel'),    
    url(r'^login/$', views.my_login, name='my_login'),    
    url(r'^logout/$', views.my_logout, name='my_logout'),    
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.myregister, name='myregister'),        
    url(r'^product/$', views.product, name='product'),

]
