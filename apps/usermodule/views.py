from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Student, Student2, Product
from .forms import StudentForm, Student2Form, ProductForm
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, 'you have successfully registered')
        return redirect('/users/login')

    return render(request, 'usermodule/register.html')


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'login successfully')
            return redirect('student_list')

        
        else:
            messages.error(request, 'invalid username or password')
            return render(request, 'usermodule/login.html')

    return render(request, 'usermodule/login.html')

def user_logout(request):

    logout(request)

    return redirect('/users/login')

# list students
@login_required(login_url='/users/login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'usermodule/student_list.html', {'students': students})


# add student
@login_required(login_url='/users/login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'usermodule/student_form.html', {'form': form})


# update student
@login_required(login_url='/users/login')
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'usermodule/student_form.html', {'form': form})


# delete student
@login_required(login_url='/users/login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'usermodule/delete_student.html', {'student': student})


# Task 2 - list students many to many
@login_required(login_url='/users/login')
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/student2_list.html', {'students': students})


# Task 2 - add student many to many
@login_required(login_url='/users/login')
def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()

    return render(request, 'usermodule/student2_form.html', {'form': form})


# Task 2 - update student many to many
@login_required(login_url='/users/login')
def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)

    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)

    return render(request, 'usermodule/student2_form.html', {'form': form})


# Task 2 - delete student many to many
@login_required(login_url='/users/login')
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')

    return render(request, 'usermodule/delete_student2.html', {'student': student})


# Task 3 - product list
@login_required(login_url='/users/login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'usermodule/product_list.html', {'products': products})


# Task 3 - add product
@login_required(login_url='/users/login')
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'usermodule/product_form.html', {'form': form})