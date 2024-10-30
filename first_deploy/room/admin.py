from django.contrib import admin

from room.models import Room, Student


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'capacity', ]
    search_fields = ['name', ]
    list_filter = ['year', ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'year', 'room', ]
