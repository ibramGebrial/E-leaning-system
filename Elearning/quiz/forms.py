from django.forms import ModelForm
from .models import Quiz, Question, Answer
from django import forms


class quizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'marksToPass',
                  'time', 'attempts','numberOfQuestions']
 

   

    def __init__(self, *args, **kwargs):
        super(quizForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  description'})
        self.fields['marksToPass'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['time'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['attempts'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['numberOfQuestions'].widget.attrs.update(
            {'class': 'form-control'})



        
class questionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_title']

    def __init__(self, *args, **kwargs):
        super(questionForm, self).__init__(*args, **kwargs)

        self.fields['question_title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  Your question'})  


class answerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_option','correct_answer']

    def __init__(self, *args, **kwargs):
        super(answerForm, self).__init__(*args, **kwargs)

        self.fields['answer_option'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  Your question'})             