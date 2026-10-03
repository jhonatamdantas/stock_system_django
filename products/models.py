from django.db import models

# Create your models here.
class HardwareProduct(models.Model):
    class Category(models.TextChoices):
        MEMORY_RAM = "Memória Ram"
        PROCESSOR = "Processador"
        VIDEO_CARD = "Placa de Vídeo"
        PERIPHERALS = "Periféricos"
        MOTHERBOARD = "Placa Mãe"
        MONITOR = "Monitor"

    id = models.AutoField(primary_key=True, unique=True, serialize=False)
    name = models.CharField(max_length=100, null=False)
    type_product = models.CharField(max_length=100, choices=Category.choices, default=Category.MEMORY_RAM, null=False)
    stock = models.IntegerField(null=False)
    cost_price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)