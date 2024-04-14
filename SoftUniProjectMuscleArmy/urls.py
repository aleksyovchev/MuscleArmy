from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SoftUniProjectMuscleArmy.common.urls')),
    path('accounts/', include('SoftUniProjectMuscleArmy.accounts.urls')),
    path('articles/', include('SoftUniProjectMuscleArmy.articles.urls')),
    path('products/', include('SoftUniProjectMuscleArmy.products.urls')),
]