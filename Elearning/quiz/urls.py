from django.urls import path
from . import views


urlpatterns = [
    path('quiz-detail/<str:pk>/', views.quizDetail, name="quiz-detail"),
    path('quiz-display/<str:pk>/', views.startQuiz, name="quiz-display"),
    path('quiz-display/<pk>/save/', views.submitQuizView, name="quiz-save"),
    path('view-attemp/<str:pk>/', views.ViewAttemp, name="view-attemp"),
    path('add-quiz/<str:pk>/', views.createQuiz, name="add-quiz"),
    path('add-question/<str:pk>/', views.createQuestion, name="add-question"),
    path('add-answer/<str:pk>/', views.createAnswer, name="add-answer"),
    
]
