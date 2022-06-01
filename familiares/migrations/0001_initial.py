# Generated by Django 4.0.4 on 2022-05-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField(max_length=8)),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('hijos', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
