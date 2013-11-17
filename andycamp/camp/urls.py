from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .models import Attendant, Team
from .forms import AttendantForm, TeamForm

urlpatterns = patterns('',
    url(r'^$', CreateView.as_view(
        model=Attendant,
        #template_name="wait.html",
        template_name="index.html",
        form_class=AttendantForm,
        success_url='/registrado/'
    ), name="root"),

    url(r'^registrado/$', TemplateView.as_view(
        template_name="camp/register_success.html"
    ), name="register_success"),

    url(r'^registrado/hackaton/$', TemplateView.as_view(
        template_name="camp/hackaton_success.html"
    ), name="hackaton_success"),

    url(r'^cronograma/$', TemplateView.as_view(
        template_name="camp/cronogram.html"
    ), name="cronogram"),

    url(r'^creditos/$', TemplateView.as_view(
        template_name="camp/credits.html"
    ), name="credits"),

    url(r'^hackaton/$', CreateView.as_view(
        model=Team,
        #template_name="wait.html",
        template_name="hackaton.html",
        form_class=TeamForm,
        success_url='/registrado/hackaton/'
    ), name="hackaton"),
)


