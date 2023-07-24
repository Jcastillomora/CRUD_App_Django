# Generated by Django 4.1.1 on 2023-07-23 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_producto_f_fabricacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='laboratorio',
        ),
        migrations.AddField(
            model_name='producto',
            name='laboratorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratorio.laboratorio'),
        ),
    ]
