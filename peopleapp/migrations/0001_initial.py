# Generated by Django 4.1.1 on 2022-12-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('secondname', models.CharField(max_length=128)),
                ('bio', models.TextField()),
            ],
        ),
    ]
