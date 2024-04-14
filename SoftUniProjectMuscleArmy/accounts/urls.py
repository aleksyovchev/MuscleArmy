from django.urls import path, include

from SoftUniProjectMuscleArmy.accounts.views import SignInView, SingUpView, SignOutView, UsedDetailsView, \
    EditUserView, DeleteUserView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SingUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UsedDetailsView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
]