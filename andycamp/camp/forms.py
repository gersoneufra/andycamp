#-*- encoding:utf-8 -*-
from django import forms
from django.forms import  widgets
from .models import Attendant, Question, DEPARTMENT_CHOICES, Team


class AttendantForm(forms.ModelForm):
    first_name=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre Completo'
    }))

    last_name=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Apellidos'
    }))

    email=forms.EmailField(label='',widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Escribe tu correo aquí'
    }))

    organization= forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Organización'
    }))

    department=forms.ChoiceField(
        label='',
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={
            'class':'form-control',
        }
    ))

    assist=forms.BooleanField(
        label='',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class':'check-droid hidden',
        }
    ))

    class Meta:
        model = Attendant


class QuestionForm(forms.Form):
    name=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre Completo'
    }))
    email=forms.EmailField(label='',widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Escribe tu correo aquí'
    }))
    message=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'rows':'3',
            'cols':'13'
    }))

class TeamForm(forms.ModelForm):
    team_name = forms.CharField(
        label='Nombre del equipo',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre del equipo'
    }))

    organization = forms.CharField(
        label='Organización',
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control jump-line',
            'placeholder':'Organización'
    }))

    first_name = forms.CharField(
        label='Integrante no. 1',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre Completo'
    }))

    first_ci = forms.IntegerField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Carnet de Identidad'
    }))

    first_mail = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control jump-line',
            'placeholder': 'Correo Electrónico'
    }))

    second_name = forms.CharField(
        label='Integrante no. 2',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre Completo'
    }))

    second_ci = forms.IntegerField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Carnet de Identidad'
    }))

    second_mail = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control jump-line',
            'placeholder': 'Correo Electrónico'
    }))


    third_name = forms.CharField(
        label='Integrante no. 1',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nombre Completo'
    }))

    third_ci = forms.IntegerField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Carnet de Identidad'
    }))

    third_mail = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
    }))
    class Meta:
        model = Team
        exclude = ('position','app_name','app_image','app_description',)