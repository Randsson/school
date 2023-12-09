from django.shortcuts import render
from .models import Student

def students_home(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'students_home.html', context)