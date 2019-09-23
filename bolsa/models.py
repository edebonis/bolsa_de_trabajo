from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    relacionado = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.nombre


class Oportunidad(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(max_length=5000, null=True, blank=True)
    visible = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(default=now, null=True, blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.tipo, self.user)

    class Meta:
        verbose_name_plural = "Oportunidades"


class Profile(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # first_name = models.CharField(max_length=30, null=False, blank=False, help_text='Campo Obligatorio')
    # last_name = models.CharField(max_length=30, null=False, blank=False, help_text='Campo Obligatorio')
    is_staff = User.is_staff
    es_alumno = models.BooleanField(default=True, null=False)
    es_oferente = models.BooleanField(default=False, null=False)
    telefono = models.CharField(max_length=30, null=False, blank=False, help_text='Campo obligatorio')

    def __str__(self):
        return '{} - {}'.format(self.first_name, self.email)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
