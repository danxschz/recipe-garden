from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.urls import reverse, reverse_lazy

# Create your views here.
def Main(request):
    template_name = 'home/main.html'
    return render(request, template_name)

class SignUp(View):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home:main')

    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Haven't set messages
            messages.success(request, 'Your account has been successfully created.')
            return redirect(self.success_url)
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
            context = {'form': form}
            return render (request, self.template_name, context)