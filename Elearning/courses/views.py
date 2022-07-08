from django.contrib import messages
from .forms import courseForm, lessonForm, videoForm, bookForm, reviewForm, materialForm, certificateForm
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Course, Tag, Lesson, Video, Book,Category,Review,Material, Certificate
from .utils import searchCourses, paginationCourses
from rest_framework.decorators import api_view
from rest_framework.response import Response


    
def home(request):
    categories = Category.objects.all()
    
    return render(request, 'index.html',{'categories': categories})

def Categories(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}
	return render(request, 'courses/sub-category.html', context)

def CategoryView(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(id=pk)
    courses = Course.objects.filter(category=category)
    context = {
		'category': category,
		'courses': courses,
        'categories': categories,
	}
    return render(request, 'courses/sub-category.html', context)

def courses(request):
    categories = Category.objects.all()
    courses, search = searchCourses(request)
    custom_range, courses = paginationCourses(request, courses, 6)  
    context = {'courses': courses, 'search': search,
               'custom_range': custom_range,'categories':categories}
    return render(request, 'courses/courses.html', context)


def course(request, pk):
    categories = Category.objects.all()
    courseObj = Course.objects.get(id=pk)
    reviews=Review.objects.filter(course=courseObj)
    context={'course': courseObj,'categories':categories,'reviews':reviews}
    return render(request, 'courses/course-detail.html',context )

# lesson


def lesson(request):
    lesson = Lesson.objects.all()
    context = {'lesson': lesson}
    return render(request, 'courses/course-detail.html', context)


@login_required(login_url='login')
def createLesson(request, pk):
    lessonObj = Course.objects.get(id=pk)
    form = lessonForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = lessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.courses = lessonObj
            messages.success(request, 'Lesson was created!')
            lesson.save()
            return redirect('course', pk=lessonObj.id)
    context = {'lesson': lessonObj, 'form': form}
    return render(request, 'lesson/lesson-form.html', context)

# book


@login_required(login_url='login')
def bookDisplay(request, pk):
    bookObj = Book.objects.get(id=pk)
    return render(request, 'lesson/book-display.html', {'book': bookObj})


@login_required(login_url='login')
def addBook(request, pk):
    bookObj = Lesson.objects.get(id=pk)
    form = bookForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            lessons = Book.objects.all()
            book.lessons.add = (lessons)
            messages.success(request, 'Book was created!')
            book.save()
            book.lessons.add(bookObj)
        else:
            messages.warning(request, "Book wasn't created!")

    context = {'video': bookObj, 'form': form}
    return render(request, 'lesson/book-form.html', context)


# Video


@login_required(login_url='login')
def videoDisplay(request, pk):
    videoeObj = Video.objects.get(id=pk)
    return render(request, 'lesson/video-display.html', {'video': videoeObj})


@login_required(login_url='login')
def addVideo(request, pk):

    videoObj = Lesson.objects.get(id=pk)
    form = videoForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.lessons = videoObj
            messages.success(request, 'Video was created!')
            video.save()
        else:
            messages.warning(request, "Video wasn't created!")

    context = {'video': videoObj, 'form': form}
    return render(request, 'lesson/video-form.html', context)

# Material

@login_required(login_url='login')
def materialDisplay(request, pk):
    materialObj = Material.objects.get(id=pk)
    return render(request, 'lesson/material-display.html', {'material': materialObj})


@login_required(login_url='login')
def addMaterial(request, pk):

    materialObj = Lesson.objects.get(id=pk)
    form = materialForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = materialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.lessons = materialObj
            messages.success(request, 'Material was created!')
            material.save()
        else:
            messages.warning(request, "Material wasn't created!")

    context = {'material': materialObj, 'form': form}
    return render(request, 'lesson/material-form.html', context)

# Certificate
@login_required(login_url='login')
def certificateDisplay(request, pk):
    certificateObj = Certificate.objects.get(id=pk)
    course=Course.objects.all()
    profile = request.user.profile
    course.owner=profile
    certificateObj.student=profile
    return render(request, 'lesson/certificate-display.html',{'certificate': certificateObj,'course':course})




@login_required(login_url='login')
def addCertificate(request, pk):

    certificateObj = Course.objects.get(id=pk)
    form = certificateForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = certificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.course = certificateObj
            messages.success(request, 'Material was created!')
            certificate.save()
        else:
            messages.warning(request, "Material wasn't created!")

    context = {'certificate': certificateObj, 'form': form}
    return render(request, 'lesson/certificate-form.html', context)

# Course

@login_required(login_url='login')
def createCourse(request):
    categories = Category.objects.all()
    profile = request.user.profile
    form = courseForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        addtags = request.POST.get('addtags').replace(',', " ").split()
        form = courseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = profile
            course.save()
            for tag in addtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                course.tags.add(tag)
            return redirect('courses')
    context = {'form': form}
    return render(request, 'courses/course-form.html', context)


@login_required(login_url='login')
def updateCourse(request, pk):
    profile = request.user.profile
    course = profile.course_set.get(id=pk)
    form = courseForm(instance=course)
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        addtags = request.POST.get('addtags').replace(',', " ").split()
        form = courseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save()
            for tag in addtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                course.tags.add(tag)
            return redirect('account')
    context = {'form': form, 'course': course}
    return render(request, 'courses/course-form.html', context)


@login_required(login_url='login')
def deleteCourse(request, pk):
    profile = request.user.profile
    course = profile.course_set.get(id=pk)
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        course.delete()
        messages.success(request, 'Course was deleted!')
        return redirect('account')
    context = {'object': course}
    return render(request, 'courses/delete_template.html', context)

# Tag


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    courseId = request.data['course']

    course = Course.objects.get(id=courseId)
    tag = Tag.objects.get(id=tagId)

    course.tags.remove(tag)

    return Response('Tag was deleted!')


@login_required
def Enroll(request, pk):
    profile = request.user.profile
    course = Course.objects.get(id=pk)
    course.students.add(profile)
    return render(request, 'courses/course-detail.html', {'course': course})


@login_required 
def addReview(request,pk):
    courseObj = Course.objects.get(id=pk)   
    form = reviewForm()

    if request.method == 'POST':
       
        form = reviewForm(request.POST)
        if form.is_valid():
            data = reviewForm()
            review = form.save(commit=False)
            data.title = form.cleaned_data['title']
            data.rate = form.cleaned_data['rate']
            data.body = form.cleaned_data['body']
            review.course = courseObj
            review.owner = request.user.profile
            review.save()
            
            messages.success(request, 'Your review was successfully submitted!')
            return redirect('course', pk=courseObj.id)
    return render(request, 'courses/course-detail.html', {'course': courseObj, 'form': form})