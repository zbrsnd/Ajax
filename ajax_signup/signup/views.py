from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


class SignUpView(CreateView):
    template_name = 'signup/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy('home')


def home(request):
    return render(request, 'signup/home.html')
