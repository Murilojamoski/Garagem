from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    modelo = models.ForeignKey('Modelo', on_delete=models.PROTECT, related_name='veiculos')
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT, related_name='veiculos')
    acessorios = models.ManyToManyField('Acessorio', related_name='veiculos')

    def __str__(self):
        return f'{self.id} - {self.modelo.nome.upper()} - {self.cor.nome.upper()} - {self.ano}'