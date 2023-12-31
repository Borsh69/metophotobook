# Generated by Django 4.0.2 on 2023-10-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_user_unique_together_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photoes',
            field=models.ManyToManyField(related_name='+', to='base.Photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ManyToManyField(blank=True, null=True, to='base.Photo', verbose_name='Фотографии пользователя'),
        ),
    ]
