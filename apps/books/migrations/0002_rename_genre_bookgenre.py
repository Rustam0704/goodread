# Generated by Django 5.0.2 on 2024-02-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='BookGenre',
        ),
    ]
