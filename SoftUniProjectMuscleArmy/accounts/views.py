from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from SoftUniProjectMuscleArmy.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'profile/login-page.html'


class SingUpView(views.CreateView):
    template_name = 'profile/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UsedDetailsView(views.DetailView):
    template_name = 'profile/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context


class EditUserView(views.UpdateView):
    template_name = 'profile/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk
        })


class DeleteUserView(views.DeleteView):
    template_name = 'profile/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')