# Generated by Django 4.1.7 on 2023-06-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='book',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='problems',
            name='chapter',
            field=models.TextField(max_length=500),
        ),
    ]