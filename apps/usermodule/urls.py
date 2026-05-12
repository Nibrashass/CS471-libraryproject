from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('students2/', views.student2_list, name='student2_list'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/update/<int:id>/', views.update_student2, name='update_student2'),
    path('students2/delete/<int:id>/', views.delete_student2, name='delete_student2'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('users/register', views.register, name='register'),
    path('users/login', views.user_login, name='login'),
    path('users/logout', views.user_logout, name='logout'),
]