from django import forms
from .models import Trainee
from course.models import Course

class TraineeForm(forms.form):
    name = forms.CharField(max_length=100, null=False)
    age = forms.IntegerField(null=False)
    degree = forms.DecimalField(decimal_places=2,max_digits=4,null=False)
    

class TraineeFormModel(forms.ModelForm):
    class Meta:
        model= Trainee
        fields=["name", "age", "degree"]