# Generated by Django 2.2.1 on 2019-07-27 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.Teacher'),
            preserve_default=False,
        ),
    ]
