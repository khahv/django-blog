# Generated by Django 5.1.3 on 2024-11-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_machinetemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='machines',
            field=models.ManyToManyField(blank=True, to='theblog.machinetemplate'),
        ),
    ]