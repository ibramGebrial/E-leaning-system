from django.contrib import admin
from .models import Quiz, Question, Answer, Result
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Result)


class Answerrr(admin.TabularInline):
    model = Answer


class Questionn(admin.ModelAdmin):
    inlines = [Answerrr]


admin.site.register(Question, Questionn)
admin.site.register(Answer)
