# Generated by Django 4.1.7 on 2023-06-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.ImageField(default='', upload_to='skills')),
            ],
        ),
    ]
