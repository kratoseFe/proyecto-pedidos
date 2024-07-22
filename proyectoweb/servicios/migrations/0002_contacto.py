# Generated by Django 5.0.2 on 2024-04-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('identificacion', models.CharField(max_length=10)),
                ('profesion', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contactos',
            },
        ),
    ]