# Generated by Django 4.0.7 on 2022-09-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
