# Generated by Django 4.1.6 on 2023-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('clase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('asignatura', models.CharField(max_length=50)),
            ],
        ),
    ]