from django.db import models

# Create your models here.
#
class User(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "Usuario"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    existencia = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "Producto"


class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    placa = models.CharField(max_length=6)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.DateField()
    kilometraje = models.IntegerField()
    documento = models.CharField(max_length=10)
    
    def __str__(self):
        return self.marca , self.modelo
    
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        db_table = "Vehiculo"


class insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2)
    
    def _str__(self):
        return self.nombre, self.precio_unitario
    
    class Meta:
        verbose_name = "insumo"
        verbose_name_plural = "insumos"
        db_table = "insumo"
        
class tipo_servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    duracion_estimada = models.DateField()
    estado = models.BooleanField(default= True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "tipo_servicio"
        verbose_name_plural = "tipo_servicios"
        db_table = "tipo_servicio"
    
        































































































































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
# Create your models here.
#
class User(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45,unique=True)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "Usuario"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    existencia = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "Producto"


class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=100)
    placa = models.CharField(max_length=6)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.DateField()
    kilometraje = models.IntegerField()
    documento = models.CharField(max_length=10)
    
    def __str__(self):
        return self.marca , self.modelo
    
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        db_table = "Vehiculo"


class insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10,decimal_places=2)
    
    def _str__(self):
        return self.nombre, self.precio_unitario
    
    class Meta:
        verbose_name = "insumo"
        verbose_name_plural = "insumos"
        db_table = "insumo"
        
class tipo_servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    duracion_estimada = models.DateField()
    estado = models.BooleanField(default= True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "tipo_servicio"
        verbose_name_plural = "tipo_servicios"
        db_table = "tipo_servicio"
    
        
