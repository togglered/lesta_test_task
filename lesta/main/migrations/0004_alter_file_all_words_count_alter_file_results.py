# Generated by Django 5.1.7 on 2025-03-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_words_file_all_words_count_file_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='all_words_count',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='results',
            field=models.JSONField(null=True),
        ),
    ]
