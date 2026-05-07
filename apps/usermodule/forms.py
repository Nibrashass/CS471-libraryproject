from django import forms
from .models import Student, Address, Student2, Address2, Product


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = '__all__'


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'