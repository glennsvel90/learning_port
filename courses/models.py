from django.urls import reverse
from django.contrib import admin
from django.db import models

from django.contrib.auth.models import User

class Course(models.Model):
    """ Create Course blueprint """

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User)
    subject = models.CharField(default='', max_length=100)
    published = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def time_to_complete(self):
        """ Tell how long the course takes based on the description of the course """

        from courses.templatetags.course_extras import time_estimate
        return '{} min.'.format(time_estimate(len(self.description.split())))





class Step(models.Model):
    """ Create sequence of passage steps to complete a course """

    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title


class Text(Step):
    """ Create the text of the course as one of the steps to complete the course """

    content = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
                'course_pk': self.course_id,
                'step_pk': self.id
            })


class Quiz(Step):
    """ Create a quiz as one of the steps to complete a coures """


    total_questions = models.IntegerField(default=4)
    times_taken = models.IntegerField(default=0, editable=False)

    class Meta:
        verbose_name_plural = "Quizzes"

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
                'course_pk': self.course_id,
                'step_pk': self.id
            })


class Question(models.Model):
    """ Creates a question blueprint for a quiz """

    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order',]

    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    def __str__(self):
        return self.prompt

class MultipleChoiceQuestion(Question):
    """ Creates a multiple choice question as one of the question types """

    shuffle_answers = models.BooleanField(default=False)


class TrueFalseQuestion(Question):
    pass


class Answer(models.Model):
    """ Creates the answer for one of the questions """

    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.text
