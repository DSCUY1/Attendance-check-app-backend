# Generated by Django 3.1.2 on 2021-02-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('libelle', models.CharField(max_length=255)),
                ('localisation', models.CharField(max_length=255)),
            ],
        ),
    ]
