from django.http import HttpResponse
from .models import blogPost
from django.template import loader


def index(request):

    template = loader.get_template('blogapp/index.html')
    blog_list = blogPost.objects.all().order_by('-create_date')
    context = {'blog_list' : blog_list, 'request' : request}
    
    return HttpResponse(template.render(context, request))


def getBlog(request, id):
    template = loader.get_template('blogapp/blog.html')
    blog_content = blogPost.objects.filter(slug=id)[0]
    return HttpResponse(template.render({'blog_content' : blog_content}, request))
