# Generated by Django 2.1.5 on 2019-02-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20190228_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='vocbulary',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
