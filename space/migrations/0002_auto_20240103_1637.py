# Generated by Django 3.2.23 on 2024-01-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deskspace',
            old_name='term',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='labspace',
            old_name='term',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='deskspace',
            name='price',
        ),
        migrations.RemoveField(
            model_name='labspace',
            name='price',
        ),
        migrations.AddField(
            model_name='deskspace',
            name='termprices',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labspace',
            name='termprices',
            field=models.JSONField(default=0.0),
            preserve_default=False,
        ),
    ]
