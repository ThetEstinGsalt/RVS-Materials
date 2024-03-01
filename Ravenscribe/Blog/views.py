from django.shortcuts import render, HttpResponse
from .models import Blog, affiliate


def blog(request, sno):
    blog = Blog.objects.filter(auto_increment_id=sno)
    nexts = sno+1
    prevs = sno-1

    newblogs = int(Blog.objects.count())-9
    endslicing = newblogs+9
    lastest = Blog.objects.order_by('timestamp')[newblogs:endslicing:-1]
    affiliate1 = affiliate.objects.filter(auto_increment_id=sno)
    try:
        blog_next_title = Blog.objects.filter(auto_increment_id=sno+1)[0].title
        blog_next_image = Blog.objects.filter(
            auto_increment_id=sno+1)[0].thumbnail
        blog_prev_title = Blog.objects.filter(auto_increment_id=sno-1)[0].title
        blog_prev_image = Blog.objects.filter(
            auto_increment_id=sno-1)[0].thumbnail
    except:
        blogs = Blog.objects.count()
        if(sno-1 == 0):
            nexts = sno+1
            prevs = blogs
            blog_prev_title = Blog.objects.filter(
                auto_increment_id=blogs).first().title
            blog_prev_image = Blog.objects.filter(
                auto_increment_id=blogs).first().thumbnail
            blog_next_title = Blog.objects.filter(
                auto_increment_id=sno+1).first().title
            blog_next_image = Blog.objects.filter(
                auto_increment_id=sno+1).first().thumbnail

        else:
            nexts = blogs-(blogs-1)
            prevs = sno-1
            blog_next_title = Blog.objects.filter(
                auto_increment_id=blogs-(blogs-1)).first().title
            blog_next_image = Blog.objects.filter(
                auto_increment_id=blogs-(blogs-1)).first().thumbnail
            blog_prev_title = Blog.objects.filter(
                auto_increment_id=sno-1).first().title
            blog_prev_image = Blog.objects.filter(
                auto_increment_id=sno-1).first().thumbnail

    return render(request, 'blog.html', {'blog': blog.first(), 'affiliate': affiliate1.first(), 'recomendation': lastest, 'prev0': blog_prev_title, 'prev1': blog_prev_image, 'prev': prevs,
                                         'next': nexts, 'next0': blog_next_title, 'next1': blog_next_image})
