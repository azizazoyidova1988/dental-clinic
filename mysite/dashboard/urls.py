from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('price/list/', views.price_list, name="price_list"),
    path('price/add/', views.price_create, name="price_add"),
    path('price/<int:price_id>/edit/', views.price_edit, name="price_edit"),
    path('price/<int:price_id>/delete/', views.price_delete, name="price_delete"),

    path('testimonial/list/', views.testimonial_list, name="testimonial_list"),
    path('testimonial/add/', views.testimonial_create, name="testimonial_add"),
    path('testimonial/<int:testimonial_id>/edit/', views.testimonial_edit, name="testimonial_edit"),
    path('testimonial/<int:testimonial_id>/delete/', views.testimonial_delete, name="testimonial_delete"),

    path('service/list/', views.service_list, name="service_list"),
    path('service/add/', views.service_create, name="services_add"),
    path('service/<int:service_id>/edit/', views.service_edit, name="services_edit"),
    path('service/<int:service_id>/delete/', views.service_delete, name="services_delete"),

    path('doctor/list/', views.doctor_list, name="doctor_list"),
    path('doctor/add/', views.doctor_create, name="doctor_add"),
    path('doctor/<int:doctor_id>/edit/', views.doctor_edit, name="doctor_edit"),
    path('doctor/<int:doctor_id>/delete/', views.doctor_delete, name="doctor_delete")

   ]