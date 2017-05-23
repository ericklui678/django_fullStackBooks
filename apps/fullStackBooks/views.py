from django.shortcuts import render, redirect
from .models import Book

def index(request):
    # Book.objects.create(title='Horton Hears a Who', author='Dr. Seuss', category='children')
    # Book.objects.filter(id=5).delete()
    context = {'books': Book.objects.all()}
    return render(request, 'fullStackBooks/index.html', context)

def create(request):
    title = request.POST['title']
    category = request.POST['category']
    author = request.POST['author']
    if len(title) < 1 or len(category) < 1 or len(author) < 1:
        return redirect('/')

    Book.objects.create(title=title, category=category, author=author)
    return redirect('/')
