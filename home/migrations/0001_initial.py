# Generated by Django 3.2.23 on 2024-02-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=254)),
                ('p_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('p_link', models.CharField(max_length=254)),
            ],
        ),
    ]
