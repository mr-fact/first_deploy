from django.contrib import admin

from room.models import Room, Student


class StudentInline(admin.TabularInline):
    model = Student

    def has_change_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj):
        return False


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'capacity', ]
    search_fields = ['name', ]
    list_filter = ['year', ]
    inlines = [StudentInline, ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'year', 'room', ]
