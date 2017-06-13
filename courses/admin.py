from django.contrib import admin
from datetime import date
from django.contrib.admin import SimpleListFilter

from . import models

class TextInline(admin.StackedInline):
    model = models.Text


class QuizInline(admin.StackedInline):
    model = models.Quiz


class AnswerInline(admin.StackedInline):
    model = models.Answer


class YearListFilter(admin.SimpleListFilter):
    title = 'year created'

    parameter ='year'

    def lookups(self, request, model_admin):
        return(
            ('2016','2016'),
            ('2017','2017'),
        )

    def queryset(self, request, queryset):
        if self.value() == 2016:
            return queryset.filter(created_at__gte=date(2016,1,1),
                                   created_at__lte=date(2016,12,31))

    def queryset(self, request, queryset):
        if self.value() == 2017:
            return queryset.filter(created_at__gte=date(2017,1,1),
                                   created_at__lte=date(2017,12,31))


class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]

    search_fields = ['title', 'description']

#show fileter by 'is_live' doesn't work
    list_filter = ['created_at']

    list_display =['title', 'created_at', 'time_to_complete']

    class Media:
        js = ('js/vendor/markdown.js', 'js/preview.js')
        css = {
            'all':('css/preview.css',),
        }



class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]

    search_fields = ['prompt']

    list_display = ['prompt', 'quiz', 'order']

    list_editable = ['quiz', 'order']



class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']


#collapse doesn't work
class TextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('course', 'title', 'order', 'description')
            }),
        ('Add content', {
            'fields': ('content',),
            'classes': ('collapse',)
            })
    )


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Text)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)
