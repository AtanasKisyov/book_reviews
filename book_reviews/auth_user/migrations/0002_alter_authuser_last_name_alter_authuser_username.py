# Generated by Django 4.0.3 on 2022-04-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='last_name',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]