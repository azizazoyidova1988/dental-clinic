from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    job = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    service = models.ForeignKey(Service, max_length=150, blank=True, null=True, on_delete=models.SET_NULL)
    doctors = models.ForeignKey(Doctors, max_length=50, blank=True, null=True, on_delete=models.SET_NULL)
    appointment_day = models.CharField(max_length=50, blank=True, null=True)
    appointment_time = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name


class Oficce_Contact(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    descriptions = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.name


class Opening_hourse(models.Model):
    days = models.CharField(max_length=150, blank=True, null=True)
    times = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "opening"

    def __str__(self):
        return self.days


class Service_pricing(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    price = models.CharField(max_length=50, blank=True, null=True)
    service_1 = models.CharField(max_length=150, blank=True, null=True)
    service_2 = models.CharField(max_length=150, blank=True, null=True)
    service_3 = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "price"

    def __str__(self):
        return self.name


class Doctor_service(models.Model):
    doctor_service = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "doctor_service"

    def __str__(self):
        return self.doctor_service
