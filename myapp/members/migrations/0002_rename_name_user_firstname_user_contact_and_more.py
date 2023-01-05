# Generated by Django 4.1.5 on 2023-01-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=100, max_length=70),
            preserve_default=False,
        ),
    ]
