from django.contrib import admin
from .models import Category, Course, Review, Tag, Lesson, Video, Book,Material, Certificate

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Book)
admin.site.register(Material)
admin.site.register(Certificate)