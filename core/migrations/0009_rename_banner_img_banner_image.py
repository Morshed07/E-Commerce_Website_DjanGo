# Generated by Django 4.2.5 on 2023-09-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='banner_img',
            new_name='image',
        ),
    ]