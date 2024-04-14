from django.urls import path, include

from SoftUniProjectMuscleArmy.courses.views import details_course

urlpatterns = [
    path('course/<slug:course_slug>', include([
        path('', details_course, name='details course'),
        # path('delete/', delete_user, name='delete user'),
    ])),
]