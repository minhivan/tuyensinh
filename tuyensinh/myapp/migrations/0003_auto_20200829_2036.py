# Generated by Django 3.0.5 on 2020-08-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_registers_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upload',
        ),
        migrations.AddField(
            model_name='registers',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
