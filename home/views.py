from django.shortcuts import render

# Create your views here.
def Main(request):
    template_name = 'home/main.html'
    return render(request, template_name)
