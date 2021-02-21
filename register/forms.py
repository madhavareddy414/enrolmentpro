from django import forms

from register.models import Student


class StudentForm(forms.Form):

    sname = forms.CharField(max_length=30,label='Student Name')
    saddr = forms.CharField(max_length=30,label='Student Addr')
    sdep = forms.CharField(max_length=30,label='Student Dep')
    ssch = forms.CharField(max_length=30,label='Student School')

class SForm(forms.Form):
    sname = forms.CharField(max_length=30,label='Student Nmae' )

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('sname','saddr','sdep','ssch')
        widgets = {
            'sname':forms.TextInput(attrs={'class':'form-control','place holder':'please enter'}),
            'saddr': forms.TextInput(attrs={'class': 'form-control'}),
            'sdep': forms.TextInput(attrs={'class': 'form-control'}),
            'ssch': forms.TextInput(attrs={'class': 'form-control'}),
        }
