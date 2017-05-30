from django import template

from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    '''gets the newest course that was added to the library'''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''show a dictionary of the courses to seve as navigation pane '''
    courses = Course.objects.all()
    return {'courses': courses }