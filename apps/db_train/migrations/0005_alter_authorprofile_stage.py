# Generated by Django 4.2.5 on 2024-03-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0004_tag_entry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='stage',
            field=models.IntegerField(blank=True, default=0, help_text='Стаж в годах', verbose_name='Стаж'),
        ),
    ]
