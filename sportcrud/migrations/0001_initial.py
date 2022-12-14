# Generated by Django 4.1.2 on 2022-11-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportCrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, upload_to='video/% Y/% m/% d/')),
                ('descriptions', models.CharField(max_length=3000)),
            ],
        ),
    ]
