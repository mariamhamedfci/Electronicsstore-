# Generated by Django 4.2.5 on 2023-09-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronicsstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('price', models.FloatField(null=True)),
                ('mark', models.CharField(max_length=60, null=True)),
                ('features', models.CharField(max_length=60, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('In progress', 'In progress'), ('Out of order', 'out of ordfer')], max_length=99, null=True)),
            ],
        ),
    ]
