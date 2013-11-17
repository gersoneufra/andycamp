# -*- encoding:utf-8 -*-
from django.db import models

DEPARTMENT_CHOICES = (
    ('LP', 'La Paz'),
    ('OR', 'Oruro'),
    ('SCZ', 'Santa Cruz'),
    ('CO', 'Cochabamba'),
    ('PO', 'Potosi'),
    ('SU', 'Sucre'),
    ('TR', 'Tarija'),
    ('PA', 'Pando'),
    ('BEN', 'Beni'),
)

class Attendant(models.Model):
    first_name = models.CharField(max_length=80,
        help_text="máximo de 80 caracteres",
        verbose_name="Nombre Completo"
    )
    last_name = models.CharField(max_length=80,
        help_text="máximo de 80 caracteres",
        verbose_name="Apellidos"
    )
    email = models.EmailField(
        help_text="example@server.com",
        verbose_name="Correo Electrónico"
    )
    organization = models.CharField(max_length=80,
        help_text="máximo de 80 caracteres",
        verbose_name="Organización o Institución"
    )
    department = models.CharField(max_length=3,choices=DEPARTMENT_CHOICES,
        help_text="Elija Una opción, en Bolivia",
        verbose_name="Departamento"
    )

    assist = models.BooleanField(default=False,
        help_text="¿ Acamparas ?",
        verbose_name="¿ Acamparas ?",
        blank=True,
    )

    class Meta:
        verbose_name = 'Asistentes'
        verbose_name_plural = 'Personas que Asistirán'

    def __unicode__(self):
        return "%s %s"%(self.first_name,self.last_name)

class Question(models.Model):
    name = models.CharField(max_length=100,
        help_text="maximo de 100 caracteres",
        verbose_name="Nombre Completo"
    )
    email = models.EmailField(
        help_text="example@mail.com",
        verbose_name="Remitente"
    )
    message = models.TextField(max_length=500,
        help_text="maximo de 500 caracteres",
        verbose_name="Mensaje o Pregunta"
    )
    class Meta:
        verbose_name = 'Correo'
        verbose_name_plural = 'Correos Recibidos'

    def __unicode__(self):
        return self.email

class Team(models.Model):
    team_name = models.CharField(max_length=50,
        help_text="maximo de 50 caracteres",
        verbose_name="Nombre del Equipo",
        unique=True
    )

    organization = models.CharField(max_length=50,blank=True,null=True,
        help_text="maximo de 50 caracteres",
        verbose_name="Organización a la que representa"
    )
    position = models.IntegerField(blank=True,null=True,
        help_text="es cardinal",
        verbose_name="Posición en el hackaton"
    )
    app_name = models.CharField(max_length=100,blank=True,null=True,
        help_text="maximo de 100 caracteres",
        verbose_name="Nombre de la Aplicación que desarrollo"
    )

    app_image = models.ImageField(upload_to="apps",blank=True,null=True,
        help_text="es una imagen",
        verbose_name="Screenshot de la Aplicación"
    )

    app_description = models.CharField(max_length=140,blank=True,null=True,
        help_text="maximo de 140 caracteres",
        verbose_name="Descripción de la Aplicación"
    )


    first_name = models.CharField(max_length=50,
        help_text="maximo de 50 caracteres",
        verbose_name="Nombre Integrante 1"
    )

    first_ci = models.IntegerField(max_length=8,
        help_text="maximo de 50 caracteres",
        verbose_name="C.I. Integrante 1"
    )

    first_mail = models.EmailField(
        help_text="maximo de 50 caracteres",
        verbose_name="Mail Integrante 1"
    )


    second_name = models.CharField(max_length=50,
        help_text="maximo de 50 caracteres",
        verbose_name="Nombre Integrante 2"
    )

    second_ci = models.IntegerField(max_length=8,
        help_text="maximo de 50 caracteres",
        verbose_name="C.I. Integrante 2"
    )

    second_mail = models.EmailField(
        help_text="maximo de 50 caracteres",
        verbose_name="Mail Integrante 2"
    )


    third_name = models.CharField(max_length=50,
        help_text="maximo de 50 caracteres",
        verbose_name="Nombre Integrante 3"
    )

    third_ci = models.IntegerField(max_length=8,
        help_text="maximo de 50 caracteres",
        verbose_name="C.I. Integrante 3"
    )

    third_mail = models.EmailField(
        help_text="maximo de 50 caracteres",
        verbose_name="Mail Integrante 3"
    )

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos para el hackaton'

    def __unicode__(self):
        return self.team_name

