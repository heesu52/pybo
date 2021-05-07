from django.contrib import admin

# Register your models here.
from .models import Question

#admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)