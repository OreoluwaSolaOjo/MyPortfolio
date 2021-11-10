# Generated by Django 3.2.8 on 2021-10-21 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211021_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email_address',
            new_name='txtEmail',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='txtMsg',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='txtName',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='txtPhone',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
