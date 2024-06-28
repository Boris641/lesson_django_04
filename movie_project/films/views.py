from django.shortcuts import render, redirect
from . models import News_post
from . forms import News_postForms

# Create your views here.
def home(request):
    films = News_post.objects.all()
    return render(request,'films/home.html',{'films':films})

def new(request):
    films = News_post.objects.all()
    return render(request,'films/new.html', {'films':films})

def contacts(request):

    return render(request,'films/contacts.html')

def user(request):
    error = ""
    if request.method == 'POST':
        form = News_postForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(new)

        else:
            error = 'Данные заполнены не корректно'
    form = News_postForms()
    return render(request, 'films/user.html', {'form': form, 'error': error })
