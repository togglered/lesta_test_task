# Generated by Django 5.1.7 on 2025-03-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_file_all_words_count_alter_file_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='all_words_count',
        ),
        migrations.RemoveField(
            model_name='file',
            name='results',
        ),
    ]
