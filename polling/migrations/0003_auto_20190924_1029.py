# Generated by Django 2.2.5 on 2019-09-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0002_auto_20190924_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date publish'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=500),
        ),
    ]