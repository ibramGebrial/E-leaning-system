from django.urls import path
from . import views


urlpatterns = [

    path('index/', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    path('Categories/', views.Categories, name="Categories"),
    path('course/<str:pk>/', views.course, name="course"),
    path('createcourse/', views.createCourse, name="createcourse"),
    path('updatecourse/<str:pk>/', views.updateCourse, name="updatecourse"),
    path('deletecourse/<str:pk>/', views.deleteCourse, name="deletecourse"),
    path('remove-tag/', views.removeTag),
    path('video-display/<str:pk>/', views.videoDisplay, name="video-display"),
    path('book-display/<str:pk>/', views.bookDisplay, name="book-display"),
    path('create-lesson/<str:pk>/', views.createLesson, name="create-lesson"),
    path('add-video/<str:pk>/', views.addVideo, name="add-video"),
    path('add-book/<str:pk>/', views.addBook, name="add-book"),
    path('material-display/<str:pk>/', views.materialDisplay, name="material-display"),
    path('add-material/<str:pk>/', views.addMaterial, name="add-material"),
    path('add-certificate/<str:pk>/', views.addCertificate, name="add-certificate"),
    path('certificate-display/<str:pk>/', views.certificateDisplay, name="certificate-display"),
    path('enroll/<str:pk>/', views.Enroll, name='enroll'),
    path('category/<str:pk>/', views.CategoryView, name='category'),
    path('add-review/<str:pk>/', views.addReview, name='add-review'),

    
]


