from django import forms
from dental_clinic.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Users()
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service()
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors()
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial()
        fields = '__all__'

class PriceForm(forms.ModelForm):
    class Meta:
        model = Service_pricing()
        fields = '__all__'