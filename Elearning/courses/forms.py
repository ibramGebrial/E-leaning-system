from django.forms import ModelForm
from .models import Course, Lesson, Video, Book, Review, Material, Certificate
from django import forms


class courseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'requirements',
                  'category', 'featured_image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple

        }

    def __init__(self, *args, **kwargs):
        super(courseForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  description'})
        self.fields['requirements'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  requirements'})
        self.fields['category'].widget.attrs.update(
            {'class': 'dropdown-item'})
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control'})
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})
        # '__all__'


class lessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(lessonForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class videoForm(ModelForm):
    class Meta:
        model = Video

        fields = ['title', 'videolink']

    def __init__(self, *args, **kwargs):
        super(videoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['videolink'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  id ex. AqrVrbdX6-k'})
            
class materialForm(ModelForm):
    class Meta:
        model = Material

        fields = ['title', 'body','file']

    def __init__(self, *args, **kwargs):
        super(materialForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  body'})
        self.fields['file'].widget.attrs.update(
            {'class': 'form-control'})
class bookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['id', 'lessons']

    def __init__(self, *args, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['author'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['publish_year'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'YY-MM-DD'})
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['file'].widget.attrs.update(
            {'class': 'form-control'})


class reviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body', 'rate']
        

    def __init__(self, *args, **kwargs):
        super(reviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})

class certificateForm(ModelForm):
    class Meta:
        model = Certificate

        fields = ['title','file']

    def __init__(self, *args, **kwargs):
        super(certificateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add  title'})
        self.fields['file'].widget.attrs.update(
            {'class': 'form-control'})