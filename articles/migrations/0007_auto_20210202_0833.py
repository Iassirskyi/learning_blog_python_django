# Generated by Django 3.1.5 on 2021-02-02 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20210201_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'Entries'},
        ),
    ]
