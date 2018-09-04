
from django import forms
from students.models import Student




class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'surname', 'age', 'gender', 'section')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
