# Generated by Django 3.2.3 on 2021-05-31 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_userprofile_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
    ]