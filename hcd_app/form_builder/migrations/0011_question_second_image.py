# Generated by Django 3.2.7 on 2021-10-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0010_question_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='second_image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
