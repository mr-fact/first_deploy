from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm
from .models import Room


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            return redirect('success_url')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register_student.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
