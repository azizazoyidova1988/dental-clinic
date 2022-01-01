from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dental_clinic.models import *
from dental_clinic.forms import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    # projects = services.get_projects()
    # projects_count = services.get_projects_count()
    # engineer_count = services.get_engineer_count()
    # service_count = services.get_service_count()
    # commenter_count = services.get_commenter_count()
    #
    #
    #
    # ctx = {
    #     "projects": projects,
    #     "commenter_count": commenter_count,
    #     "service_count": service_count,
    #     "engineer_count": engineer_count,
    #     "projects_count": projects_count,
    #
    # }
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def price_list(request):
    price = services.get_price()
    ctx = {
        "price": price
    }
    return render(request, 'dashboard/price/list.html', ctx)


@login_required_decorator
def price_create(request):
    model = Service_pricing()
    form = PriceForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('price_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/price/form.html', ctx)


@login_required_decorator
def price_edit(request, price_id):
    model = Service_pricing.objects.get(id=price_id)
    form = PriceForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('price_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/price/form.html', ctx)


@login_required_decorator
def price_delete(request, price_id):
    model = Service_pricing.objects.get(id=price_id)
    model.delete()
    return redirect("price_list")


@login_required_decorator
def doctor_list(request):
    doctor = services.get_doctor()
    ctx = {
        "doctor": doctor
    }
    return render(request, 'dashboard/doctor/list.html', ctx)


@login_required_decorator
def doctor_create(request):
    model = Doctors()
    form = DoctorForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/doctor/form.html', ctx)


@login_required_decorator
def doctor_edit(request, doctor_id):
    model = Doctors.objects.get(id=doctor_id)
    form = DoctorForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/doctor/form.html', ctx)


@login_required_decorator
def doctor_delete(request, doctor_id):
    model = Doctors.objects.get(id=doctor_id)
    model.delete()
    return redirect("doctor_list")


@login_required_decorator
def testimonial_list(request):
    testimonial = services.get_testimonial()
    ctx = {
        "testimonial": testimonial
    }
    return render(request, 'dashboard/testimonial/list.html', ctx)


@login_required_decorator
def testimonial_create(request):
    model = Testimonial()
    form = TestimonialForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)


@login_required_decorator
def testimonial_edit(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    form = TestimonialForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)


@login_required_decorator
def testimonial_delete(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    model.delete()
    return redirect("testimonial_list")


@login_required_decorator
def service_list(request):
    service = services.get_service()
    ctx = {
        "service": service
    }
    return render(request, 'dashboard/service/list.html', ctx)


@login_required_decorator
def service_create(request):
    model = Service()
    form = ServiceForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('service_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/service/form.html', ctx)


@login_required_decorator
def service_edit(request, service_id):
    model = Service.objects.get(id=service_id)
    form = ServiceForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('service_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/service/form.html', ctx)


@login_required_decorator
def service_delete(request, service_id):
    model = Service.objects.get(id=service_id)
    model.delete()
    return redirect("service_list")

