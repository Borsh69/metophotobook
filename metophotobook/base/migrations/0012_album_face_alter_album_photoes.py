# Generated by Django 4.2.6 on 2023-10-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_user_photo_alter_user_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='face',
            field=models.ManyToManyField(related_name='+', to='base.photo'),
        ),
        migrations.AlterField(
            model_name='album',
            name='photoes',
            field=models.ManyToManyField(related_name='+', to='base.photo'),
        ),
    ]