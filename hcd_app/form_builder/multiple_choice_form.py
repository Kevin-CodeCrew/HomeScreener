from django import forms
from django.db.models import query
from django.forms import TextInput
from .models import Question


def Multiple_choice_helper(question):   
    options = []
    opts = question.answer_format[1:].split(" ")
    for opt in opts:
        options.append((opt, opt))
   

    class Multiple_choice_form(forms.ModelForm):
        
        answer = forms.MultipleChoiceField(
            
            choices= options,
            widget= forms.CheckboxSelectMultiple()
        )
        
        
        
        class Meta:
            model = Question
            fields = ['question','answer']
            widgets = {
           
            'question': TextInput(attrs={
                'style': ' visibility: hidden; hight: 0px;',
                'placeholder': 'question'
                }),
            
        } 
            
    return Multiple_choice_form(instance=question)