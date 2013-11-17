# -*- encoding:utf-8 -*-
import re

from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Question


def send_save_question(request):
    if request.is_ajax():
        if request.method == "POST" and  \
            request.POST['name'] and \
            request.POST['email'] and \
            request.POST['message'] and \
            re.match('^[(    a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',
                request.POST['email'].lower()):

            question = Question(
                name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message'],
            )
            question.save()
        else:
            return HttpResponse("Llene sus datos correctamente")
    else:
        raise Http404
    return HttpResponse("Su mensaje se envió Exitosamente")



