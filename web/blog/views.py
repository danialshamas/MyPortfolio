from django.shortcuts import render,get_object_or_404
from . models import Blog
# Create your views here.
def all_blog(request):
    dani = Blog.objects.order_by('-date')[:5] # if you want to show soem blog on page not all you use order_by -date for most recent blog posts simple it put you new blog on the top 
    return render(request, 'all_blogs.html', {'blogs':dani} )

def detail(request, blog_id):
    blog = get_object_or_404(Blog ,pk=blog_id)
    return render(request, 'detail.html',{'blog':blog})