# Generated by Django 5.1.5 on 2025-02-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=30)),
                ('lan', models.CharField(max_length=20)),
                ('rating', models.FloatField()),
                ('about', models.TextField()),
                ('date', models.DateField()),
                ('movieimg', models.ImageField(default='img not found', upload_to='')),
            ],
        ),
    ]
