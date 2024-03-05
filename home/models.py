# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Servizio(models.Model):

    #__Servizio_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)

    #__Servizio_FIELDS__END

    class Meta:
        verbose_name        = _("Servizio")
        verbose_name_plural = _("Servizio")


class Postazione(models.Model):

    #__Postazione_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    stato = models.CharField(max_length=255, null=True, blank=True)

    #__Postazione_FIELDS__END

    class Meta:
        verbose_name        = _("Postazione")
        verbose_name_plural = _("Postazione")


class Prenotazione(models.Model):

    #__Prenotazione_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cognome = models.CharField(max_length=255, null=True, blank=True)
    modello = models.CharField(max_length=255, null=True, blank=True)
    targa = models.CharField(max_length=255, null=True, blank=True)
    vim = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)

    #__Prenotazione_FIELDS__END

    class Meta:
        verbose_name        = _("Prenotazione")
        verbose_name_plural = _("Prenotazione")



#__MODELS__END
