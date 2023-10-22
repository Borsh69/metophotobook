# Generated by Django 4.0.2 on 2023-10-21 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
                ('photoes', models.ManyToManyField(to='base.Photo')),
            ],
        ),
    ]
