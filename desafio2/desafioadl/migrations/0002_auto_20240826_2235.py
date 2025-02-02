# Generated by Django 3.2.4 on 2024-08-27 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtarea',
            name='eliminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='eliminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subtarea',
            name='descripcion',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='subtarea',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subtarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_tarea', to='desafioadl.tarea'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
