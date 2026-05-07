from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Student2, Product
from .forms import StudentForm, Student2Form, ProductForm



# list students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'usermodule/student_list.html', {'students': students})


# add student
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
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'usermodule/delete_student.html', {'student': student})


# Task 2 - list students many to many
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/student2_list.html', {'students': students})


# Task 2 - add student many to many
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
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')

    return render(request, 'usermodule/delete_student2.html', {'student': student})


# Task 3 - product list
def product_list(request):
    products = Product.objects.all()
    return render(request, 'usermodule/product_list.html', {'products': products})


# Task 3 - add product
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'usermodule/product_form.html', {'form': form})