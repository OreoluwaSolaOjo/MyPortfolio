# Generated by Django 3.2.8 on 2021-10-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_contact_txtemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='txtEmail',
            field=models.EmailField(blank=True, max_length=70),
        ),
    ]
