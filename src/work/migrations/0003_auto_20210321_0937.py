# Generated by Django 3.1.7 on 2021-03-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20210321_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='project',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_descriptions',
            field=models.TextField(default='rezervor'),
        ),
    ]