# Generated by Django 4.0.7 on 2022-10-08 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_author_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.book'),
        ),
    ]
