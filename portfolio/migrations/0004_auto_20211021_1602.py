# Generated by Django 3.2.8 on 2021-10-21 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_contact_txtemail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='txtEmail',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='txtName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='txtMsg',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='txtPhone',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
