# Generated by Django 3.1.3 on 2022-02-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='password',
            field=models.CharField(default='1111', max_length=200),
        ),
        migrations.AlterField(
            model_name='notice',
            name='subject',
            field=models.CharField(default='', max_length=200),
        ),
    ]
