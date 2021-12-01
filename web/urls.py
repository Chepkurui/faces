# from django.urls import path
# from web import views

# # Paths
# urlpatterns = [
#     path('', views.start_page, name='start_page'),
#     path('register/', views.register, name='register'),
#     path('addFace/', views.addFace, name='addFace'), 
#     path('login/', views.login, name='login'),
#     path('welcome/(?P<face_id>\d+)/$', views.welcome, name='welcome'),
#     #path('detect/', views.detect, name='detect_image'),url(r'^welcome/(?P<face_id>\d+)/$', views.welcome)
# ]

from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
    url(r'^$', views.start_page),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^addFace/', views.addFace),
    url(r'^welcome/(?P<face_id>\d+)/$', views.welcome)
]