# Generated by Django 3.2 on 2022-06-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('N', 'none'), ('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default=False, max_length=1),
        ),
    ]
