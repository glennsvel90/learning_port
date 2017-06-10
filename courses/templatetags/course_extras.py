from django import template
from django.utils.safestring import mark_safe
import markdown2

from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    '''gets the newest course that was added to the library'''
    return Course.objects.filter(published=True).latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''show a dictionary of the courses to seve as navigation pane '''
    courses = Course.objects.filter(
        published=True
    ).order_by(
        '-created_at'
    ).values(
        'id','title'
    )[:5]
    return {'courses': courses }

@register.filter('time_estimate')
def time_estimate(word_count):
    '''estimates the time it takes to complete a course based on word count'''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
