# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render_to_response
from students.models import Student
from django.http import HttpResponseRedirect, HttpResponse
from students.forms import StudentForm

def index(request):
    sts = Student.objects.all()
    print "sts ", sts
    return render_to_response('students/index.html', {'sts': sts})

def add(request):
    print "dsgsfd"
    return render_to_response('students/add.html')

@csrf_exempt
def addstudent(request):
    created = False
    if request.method == "POST":
        student_form = StudentForm(data = request.POST)
        if student_form.is_valid():
            try:
		    student = student_form.save(commit=False)
		    student.save()
		    created = True
		    print "student added"
            except Exception, Arguement:
                    print Exception, Arguement
        else:
            print student_form.errors()
    return HttpResponseRedirect('/')


def edit(request, sid):
    s =  Student.objects.get( id = sid)
    return render_to_response('students/edit.html', {'s': s})


def delete(request, sid):
    s =  Student.objects.get( id = sid)
    s.delete()
    return HttpResponseRedirect('/')

@csrf_exempt
def editstudent(request, sid ):
    created = False
    if request.method == "POST":
        s = Student.objects.get( id = sid)
        name =  request.POST['name']
        surname =  request.POST['surname']
        age =  request.POST['age']
        section =  request.POST['class']
        gender =  request.POST['gender']
        s.name = name
        s.surname = name
        s.age = age
        s.section = section
        s.gender = gender
        s.save()
    return HttpResponseRedirect('/')
#NOTE: student id is the primary key




################

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
