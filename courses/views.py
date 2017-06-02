from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from . import forms
from . import models


def course_list(request):
    courses = models.Course.objects.all()
    email = "questions@learningport.com"
    return render(request, 'courses/course_list.html', {'courses': courses,
                                                        'email': email})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps_order = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                         key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'steps_order': steps_order
        })


def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

@login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(models.Course, pk=course_pk)
#    form = forms.Quizform()
    quiz = forms.QuizForm()
    if request.method == "POST":
#        form = forms.Quizform(request.POST)
        quiz = forms.QuizForm(request.POST)
        if quiz.is_valid():
#            quiz = form.save(commit=False)
            quiz = quiz.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.add_message(request, messages.SUCCESS, "Quiz Added!")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request,'courses/quiz_form.html', {
#       'form':form}
        'quiz':quiz,
        'course':course})

@login_required
def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk, course_id=course_pk)
    form = forms.QuizForm(intance=quiz)

    return render(request, 'courses/quiz_form.html', {'form': form, 'course':quiz.course})
