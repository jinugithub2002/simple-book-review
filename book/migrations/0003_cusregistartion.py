# Generated by Django 5.1.2 on 2024-11-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_date_tbl_book_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='cusregistartion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('number', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]