# Generated by Django 5.1 on 2024-08-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('rgm', models.CharField(max_length=20, unique=True)),
                ('periodo', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], max_length=10)),
                ('curso', models.CharField(max_length=100)),
            ],
        ),
    ]
