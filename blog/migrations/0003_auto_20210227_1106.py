# Generated by Django 3.1.2 on 2021-02-27 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commit',
            new_name='Comment',
        ),
    ]
