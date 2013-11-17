from django.contrib import admin
from .models import Attendant, Question, Team

class AttendantAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','organization','department','assist',)
    list_filer = ('department','assist')
    search_fields=('email',)

class QuestionAdmin(admin.ModelAdmin):
    search_fields=('email',"name")
    list_display = ('name','email','message',)

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('team_name',)
    list_display = ('team_name','first_name','first_ci','first_mail',
                    'second_name','second_ci','second_mail','third_name',
                    'third_ci','third_mail',)

admin.site.register(Attendant,AttendantAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Team, TeamAdmin)