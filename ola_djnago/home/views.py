from django.shortcuts import render
# Register your models here.

def home(request):
    print('home')

    context = {
        'text': 'Olá HOME'
    }
    
    return render(
        request,
        'home/index.html',
        context,
        
    )