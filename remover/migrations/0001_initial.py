# Generated by Django 4.2.1 on 2023-07-08 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ImageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_year', models.DateTimeField(verbose_name=2023)),
                ('image_month', models.DateTimeField(verbose_name=7)),
                ('image_day', models.DateTimeField(verbose_name=8)),
                ('image_name', models.CharField(blank=True, max_length=255)),
                ('image_link', models.CharField(blank=True, max_length=255)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='remover.user')),
            ],
        ),
    ]
