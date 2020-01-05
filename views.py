from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import allcourses
from django.template import loader

def Courses(request):
    ac=allcourses.objects.all()
    template=loader.get_template('App/Courses.html')
    context=    {
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def Detail(request,course_id):
    try:
        course=allcourses.objects.get(pk=course_id)
    except allcourses.DoesNotExist:
        raise Http404("Course Not Availale")
    return render(request, 'App/Detail.html',{'course':course})
# Create your views here.
