# Generated by Django 3.0.7 on 2020-11-21 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_forum', '0003_auto_20201118_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answervotes',
            options={'verbose_name_plural': 'Answer Votes'},
        ),
        migrations.AlterModelOptions(
            name='questionvotes',
            options={'verbose_name_plural': 'Question Votes'},
        ),
    ]
