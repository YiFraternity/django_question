# Generated by Django 2.0.2 on 2018-05-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_question_img_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_keyword',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='img_location',
            field=models.CharField(default='', max_length=300),
        ),
    ]
