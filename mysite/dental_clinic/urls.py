from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),
    path('team/', views.team, name='doctor'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contacts'),
    path('dashboard/', include('dashboard.urls')),
]
