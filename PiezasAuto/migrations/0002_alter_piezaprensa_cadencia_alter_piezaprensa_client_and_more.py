# Generated by Django 5.0.6 on 2024-06-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PiezasAuto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piezaprensa',
            name='Cadencia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='piezaprensa',
            name='Client',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='piezaprensa',
            name='Code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='piezaprensa',
            name='NumDoc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
