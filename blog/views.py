from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 21, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})