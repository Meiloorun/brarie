# Generated by Django 4.1.1 on 2022-12-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleapp', '0002_person_created_at_person_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]