from django.contrib import admin

from SoftUniProjectMuscleArmy.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'duration', 'length_per_day')
