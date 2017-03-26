from django.conf.urls import include, url
from django.contrib import admin
from inventory import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add', views.addBooks, name='add'),
    url(r'^low', views.lowBookList, name='lowBookList'),
    url(r'^checkOut/(?P<book_id>\d+)/', views.checkOut, name='checkOut'),
    url(r'^checkIn/(?P<book_id>\d+)/', views.checkIn, name='checkIn'),
]
