from email.policy import default

from django import forms, shortcuts
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Count, F

from first_deploy.settings import CURRENT_YEAR
from .models import Student, Room

class StudentRegistrationForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(label='رمز عبور')
    room = forms.ModelChoiceField(
        queryset=Room.objects.filter(year=CURRENT_YEAR)
        .annotate(student_count=Count('students'))
        .filter(student_count__lt=F('capacity')),
        label="نام اتاق"
    )

    def clean(self):
        cleaned_data = super().clean()
        try:
            user = User.objects.get(username=cleaned_data['username'])
        except User.DoesNotExist:
            raise ValidationError('user not found')

        if not user.check_password(cleaned_data['password']):
            raise ValidationError('incorrect password')

        students = Student.objects.filter(
            user=user,
            year=CURRENT_YEAR,
            room=None
        )
        if not students.exists():
            raise ValidationError('you have not any active room')

        student = students.first()
        room = cleaned_data['room']

        if not room.capacity_is_free():
            raise ValidationError('room has not any free space')

        student.room = room
        student.save()
