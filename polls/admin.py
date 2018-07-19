from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# Models that can be used for CRUD applications
# on admin.

#admin.site.register(Question)
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): 
    # Makes the pub date come before the question field
    #fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)