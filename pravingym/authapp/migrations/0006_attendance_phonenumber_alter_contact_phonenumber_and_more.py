# Generated by Django 4.2.7 on 2024-03-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
