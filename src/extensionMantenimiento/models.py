from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class ExtensionMantenimiento(models.Model):
    fecha = models.DateField(
        _('fecha'),
        help_text=_('fecha de la extension')
    )

    fechaFinPrevista = models.DateField(
        _('fechaFinPrevista'),
        help_text="fecha fin prevista"
    )

    motivo = models.CharField(
        _('motivo'),
        max_length=200,
        help_text="motivo de la extension"
    )

    class Meta:
        ordering = ['fecha','fechaFinPrevista','motivo']
        verbose_name = 'extension mantenimiento'
        verbose_name_plural = 'extensiones mantenimiento'
