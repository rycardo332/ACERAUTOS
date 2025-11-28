from django.db import models

# Create your models here.















































































class GestionNotificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=45)
    fecha_envio = models.CharField(max_length=45)
    fk_ventas = models.ForeignKey('Venta', on_delete=models.CASCADE)

    def __str__(self):
        return f"Notificación {self.id_notificacion} - {self.mensaje}"

    class Meta:
        verbose_name = "Gestión de Notificación"
        verbose_name_plural = "Gestión de Notificaciones"
        db_table = "gestion_notificacion"
        
    

class CategoriaProductos(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    fk_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"
        db_table = "categoria_productos"
        
        

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10)  

    fk_proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fk_insumo = models.ForeignKey('Insumo', on_delete=models.CASCADE)

    def __str__(self):
        return f"Compra {self.id_compra} - {self.estado}"

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        db_table = "compra"


