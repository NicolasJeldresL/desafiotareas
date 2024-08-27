from django.db import models

class Tarea(models.Model):
    descripcion = models.TextField(max_length=500, default='')
    estado = models.BooleanField(default=False)
    eliminada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    descripcion = models.TextField(max_length=500, default='')
    estado = models.BooleanField(default=False)
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='sub_tarea', on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
