from django.db import models

# Create your models here.

class Factura(models.Model):
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    iva = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    venta = models.ForeignKey('Venta',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.total , self.venta.fecha
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        db_table = "Factura"