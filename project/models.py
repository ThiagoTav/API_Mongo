from django.db import models

class Clima(models.Model):
    cidade = models.CharField(max_length=255)
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    condicao = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cidade} - {self.temperatura}°C ({self.condicao})"

class HistoricoClima(models.Model):
    clima = models.ForeignKey(Clima, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.clima.cidade} - {self.clima.temperatura}°C ({self.clima.condicao}) - {self.data_hora}"
