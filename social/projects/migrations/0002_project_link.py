# Generated by Django 4.0.5 on 2022-06-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='', max_length=300),
        ),
    ]
