

# from .forms import courseForm, lessonForm, videoForm, bookForm
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Quiz, Answer, Result
from courses.models import Lesson, Course
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import quizForm,questionForm, answerForm
from django.contrib import messages
# Create your views here.


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def quizDetail(request, pk):
    profile = request.user.profile
    quiz = Quiz.objects.get(id=pk)
    context = {'quiz': quiz,'profile':profile}
    return render(request, 'quiz-detail.html', context)


def startQuiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    quiz.attempts -= 1
    Quiz.objects.update(attempts=quiz.attempts)
    context = {'quiz': quiz}
    return render(request, 'quiz-display.html', context)


def ViewAttemp(request,pk):
    quiz=Quiz.objects.get(id=pk)
    profile = request.user.profile
    attemp = profile.result_set.all()
    context = {'profile': profile, 'attemp': attemp,'quiz':quiz}
    return render(request, 'quiz-result.html', context)   


    


@login_required(login_url='login')
def createQuiz(request, pk):
    profile = request.user.profile
    quizObj = Lesson.objects.get(id=pk)
    form = quizForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        form = quizForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.lesson = quizObj
            quiz.owner = profile
            messages.success(request, 'Quiz was created!')
            quiz.save()
            return redirect('courses')
    context = {'quiz': quizObj, 'form': form}
    return render(request, 'quiz-form.html', context)



@login_required(login_url='login')
def createQuestion(request, pk):
    questionObj = Quiz.objects.get(id=pk)
    questionform = questionForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        questionform = questionForm(request.POST, request.FILES)
        if questionform.is_valid():
            question = questionform.save(commit=False)
            question.quiz=questionObj
            messages.success(request, 'Question was created!')
            question.save()
            return redirect('add-answer', pk=question.id)           
    context = {'question': questionObj, 'questionform': questionform}
    return render(request, 'question-form.html', context)

@login_required(login_url='login')
def createAnswer(request, pk):
    answerObj = Question.objects.get(id=pk)
    answerform = answerForm()
    if request.method == 'POST' and request.user.profile.is_teacher == True:
        answerform = answerForm(request.POST, request.FILES)
        if answerform.is_valid():
            data = answerForm()
            # data.answer_option = answerform.cleaned_data['answer_option']
            # data.correct_answer = answerform.cleaned_data['correct_answer']
            data.answer_option = request.POST.getlist('answer_option')
            data.correct_answer = request.POST.getlist('answer_option')
            answer = answerform.save(commit=False)
            answer.question = answerObj
            messages.success(request, 'Answer was created!')
            answer.save()
    context = {'answer': answerObj, 'answerform': answerform}
    return render(request, 'answer-form.html', context)

def submitQuizView(request, pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        profile = request.user.profile
        quiz = Quiz.objects.get(id=pk)

        questions = []
        mydata = request.POST
        mydata2 = dict(mydata.lists())
        mydata2.pop('csrfmiddlewaretoken')

        for q in mydata2.keys():
            print('key: ', q)
            question = Question.objects.get(question_title=q)
            questions.append(question)
        print(questions)
        marks = 0
        percentage = 100/quiz.numberOfQuestions
        results = []
        correct_answer = None
        for x in questions:
            aselected = request.POST.get(str(x.question_title))
            if aselected != "":
                answers = Answer.objects.filter(question=x)
                for a in answers:
                    if aselected == a.answer_option:
                        if a.correct_answer:
                            marks += 1
                            correct_answer = a.answer_option
                    else:
                        if a.correct_answer:
                            correct_answer = a.answer_option
                results.append(
                    {str(x): {'correct_answer': correct_answer, 'answered': aselected}})
            else:
                results.append({str(x): 'not answered'})
        markpercentage = marks*percentage
        Result.objects.create(quiz=quiz, student=profile,
                              marks=markpercentage)

        if markpercentage >= quiz.marksToPass:
            return JsonResponse({'passed': True, 'marks': markpercentage, 'results': results})
        else:
            return JsonResponse({'passed': False, 'marks': markpercentage, 'results': results})



