from django.shortcuts import render, redirect
from .models import *
from .services import *
from .forms import *


def home(request):
    services = get_services()
    doctors = get_doctor()
    testimonials = get_testimonials()
    hours = get_hours()
    doctor_service = get_doctor_service()
    prices = get_price()
    ctx = {
        "home": "active",
        'services': services,
        'doctors': doctors,
        'testimonials': testimonials,
        'hours': hours,
        'doctor_service': doctor_service,
        'prices': prices,

    }
    return render(request, 'dental_clinic/index.html', ctx)


def about(request):
    doctor_service = get_doctor_service()
    ctx = {
        "about": "active",
        'doctor_service': doctor_service,

    }
    return render(request, 'dental_clinic/about.html', ctx)


def service(request):
    services = get_services()
    ctx = {
        "service": "active",
        'services': services,

    }
    return render(request, 'dental_clinic/service.html', ctx)


def price(request):
    prices = get_price()

    ctx = {
        "price": "active",
        'prices': prices,

    }
    return render(request, 'dental_clinic/price.html', ctx)


def team(request):
    doctors = get_doctor()
    ctx = {
        "doctor": "active",
        'doctors': doctors,

    }
    return render(request, 'dental_clinic/team.html', ctx)


def testimonial(request):
    testimonials = get_testimonials()
    ctx = {
        "testimonial": "active",
        'testimonials': testimonials,

    }
    return render(request, 'dental_clinic/testimonial.html', ctx)


def appointment(request):
    model = Users()
    form = UserForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    services = get_services()
    ctx = {
        "appointment": "active",
        'services': services,

    }
    return render(request, 'dental_clinic/appointment.html', ctx)


def contact(request):
    contact = get_contact()
    ctx = {
        "contacts": "active",
        'contact': contact,

    }
    return render(request, 'dental_clinic/contact.html', ctx)
