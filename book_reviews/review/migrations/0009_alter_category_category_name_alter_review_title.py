# Generated by Django 4.0.3 on 2022-04-08 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=250, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]