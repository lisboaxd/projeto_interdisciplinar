from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, FormView
from django.shortcuts import render


from .forms import UserForm, UserProfileInfoForm
from products.forms import DonorForm, CompanyForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            dados = request.POST.copy()
            dados['user'] = user
            profile_form = UserProfileInfoForm(data=dados)
        if profile_form.is_valid():
            profile = profile_form.save()
            type_user = ''
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            if request.POST.get('tipo') == '0':
                type_user = DonorForm(data={'user':profile})
            else:
                type_user = CompanyForm(data={'user':profile})
            if type_user.is_valid():
                type_user.save()
                profile.save()
                registered = True

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,"registration/register.html",
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

class ProfileView(FormView):
    template_name = 'profile/form.html'
    form_class = UserProfileInfoForm
