# Generated by Django 3.0.5 on 2020-08-31 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200831_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
