from django.urls import path
from .import views

urlpatterns = [
    path('students/',views.get_students),
    path('student/add/',views.create_student),
    path('student/update/<int:id>/',views.update_student),
    path('student/delete/<int:id>/',views.delete_student),
]
