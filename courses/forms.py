from django import forms

from . import models


class QuizForm(forms.Modelform):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description'
            'order'
            'total_questions'
        ]
class TrueFalseQuestionForm(forms.Modelform):
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt',]
        #put correct soon as new feature

class MultipleChoiceQuestionForm(forms.Modelform):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'prompt',
            'order',
            'shuffle_answers'
        ]
