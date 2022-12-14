# Generated by Django 4.1.1 on 2022-12-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleapp', '0001_initial'),
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='producers',
            field=models.ManyToManyField(related_name='producers', to='peopleapp.person'),
        ),
        migrations.AddField(
            model_name='song',
            name='writers',
            field=models.ManyToManyField(related_name='songwriters', to='peopleapp.person'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(related_name='artists', to='peopleapp.person'),
        ),
    ]
