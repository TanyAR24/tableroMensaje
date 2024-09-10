from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DescripcionMensaje(models.Model):
    textoMensaje=models.TextField()
    remitente=models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    destinatario=models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    fechaEnvio=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Mensaje de {self.remitente} para {self.destinatario}")