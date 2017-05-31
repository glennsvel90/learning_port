from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

def hello_world(request):
    return render (request, 'home.html')


def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == "POST":
        form = form.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                'suggestion from {name} <{email}> \nto Glenn Velupillai <glennselwynvel@gmail.com>'.format(**form.cleaned_data),
                form.cleaned_data['suggestion'],
            )
            messages.add_message(request, messages.SUCCESS, 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion_view'))
    return render(request, 'suggestion_form.html', {'form':form})
