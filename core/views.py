from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, FormView, edit, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from .forms import UserForm, UserProfileInfoForm
from products.forms import DonorForm, CompanyForm
from products.models import CompanyAssociate
from .models import UserProfileInfo


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.profile_pic = ''
            if request.POST.get('tipo') == '0':
                user.save()
                type_user = DonorForm(data={'user':user})
            else:
                user.save()
                type_user = CompanyForm(data={'user':user})
            if type_user.is_valid():
                type_user.save()
                registered = True
    else:
        user_form = UserProfileInfoForm()
    return render(request,"registration/register.html",
                          {'user_form':user_form,
                           'registered':registered})

class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/form.html'
    model=UserProfileInfo
    form_class = UserProfileInfoForm
    success_url = '/'

    def get_object(self):
        return self.request.user


class PartnersListView(LoginRequiredMixin, ListView):
    model = CompanyAssociate
    template_name = 'partners/list.html'