# Generated by Django 4.0.6 on 2022-08-21 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='books',
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('book', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.book')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(related_name='items', to='core.shoppingcartitem'),
        ),
    ]
