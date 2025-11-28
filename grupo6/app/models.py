






























































































































class Entrada_Vehiculo(models.Model):
    documento = models.IntegerField()
    fecha_hora_entrada = models.DateTimeField()
    placa = models.CharField(max_length=6)

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
        
class Ventas(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10,decimal_places=2) 
    documento = models.CharField(max_length=10)
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    salida = models.ForeignKey('Salida_vehiculo',on_delete=models.CASCADE)   
    productos = models.ForeignKey('Producto',on_delete=models.CASCADE) 
    usuario = models.ForeignKey('User',on_delete=models.CASCADE)     
    
    
    def __str__(self):
        return self.fecha , self.cliente
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        db_table = "Venta"
        

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    documento = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    mercancia = models.ForeignKey('Producto',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedor"