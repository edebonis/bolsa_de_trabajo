from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    relacionado = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.nombre


class Oportunidad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)
    visible = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.tipo, self.user)

    class Meta:
        verbose_name_plural = "Oportunidades"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
