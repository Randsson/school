from django.shortcuts import render
from .models import Student
from django.views.generic import ListView

class StudentListView(ListView):
    queryset = Student.objects.all()
    template_name = 'students_home.html'
    context_object_name = 'students'

