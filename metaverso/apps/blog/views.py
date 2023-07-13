from django.shortcuts import render

# Create your views here.

def index_blog(request):
    template_name = 'blog/blog_index.html'
    return render(request,template_name)
