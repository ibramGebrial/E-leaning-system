from django.db import models
import uuid
from users.models import Profile
from django.db.models import Avg, Count

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    id =models.SlugField(unique=True, primary_key=True)

    
    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    requirements = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    rate_total = models.IntegerField(default=0, null=True, blank=True)
    rate_ratio = models.IntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(
        Profile, related_name="studentEnroll", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    
    def avgreview(self):
        reviews = Review.objects.filter(course=self).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return  avg
        
    
    def countreview(self):
        reviews = Review.objects.filter(course=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count





class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    courses = models.ForeignKey(
        Course, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    publish_year = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='books/')
    lessons = models.ManyToManyField('Lesson', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    videolink = models.CharField(max_length=200)
    lessons = models.ForeignKey(
        Lesson, null=True, blank=True, on_delete=models.SET_NULL)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Material(models.Model):
    title = models.CharField(max_length=200)
    body= models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='material/',null=True, blank=True)
    lessons = models.ForeignKey(
        Lesson, null=True, blank=True, on_delete=models.SET_NULL)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.body


class Certificate(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    course=models.ForeignKey(
        Course, null=True, blank=True, on_delete=models.CASCADE)
    student = models.OneToOneField(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='media/certificate', null=True, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.title