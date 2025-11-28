



































































































































class Entrada_Vehiculo(models.Model):
    documento = models.IntegerField()
    fecha_hora_entrada = models.DateTimeField()
    placa = models.CharField(max_length=6)

    def __str__(self):
        return f"Entrada {self.placa} - {self.fecha_hora_entrada}"

    class Meta:
        db_table = "entrada_vehiculo"
        verbose_name = "Entrada de Vehículo"
        verbose_name_plural = "Entradas de Vehículos"

class Salida_Vehiculo(models.Model):
    entrada = models.ForeignKey('Entrada_Vehiculo', on_delete=models.CASCADE)
    fecha_hora_salida = models.DateTimeField()
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Salida {self.entrada.placa} - ${self.total_a_pagar}"

    class Meta:
        db_table = "salida_vehiculos"
        verbose_name = "Salida de Vehículo"
        verbose_name_plural = "Salidas de Vehículos"

class Servicio(models.Model):
    descripcion = models.CharField(max_length=255)
    duracion = models.IntegerField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    documento = models.IntegerField()

    entrada = models.ForeignKey('Entrada_Vehiculo', on_delete=models.CASCADE)
    insumo = models.ForeignKey('Insumos', on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)
    tipo_servicio = models.ForeignKey('TipoServicio', on_delete=models.CASCADE)

    def __str__(self):
        return f"Servicio {self.descripcion} (${self.precio})"

    class Meta:
        db_table = "servicios"
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

