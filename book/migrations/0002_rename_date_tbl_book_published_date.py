# Generated by Django 5.1.2 on 2024-11-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_book',
            old_name='date',
            new_name='published_date',
        ),
    ]