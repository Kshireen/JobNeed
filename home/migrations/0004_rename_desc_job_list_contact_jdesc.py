# Generated by Django 4.2.4 on 2023-09-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_name_job_list_contact_fname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_list_contact',
            old_name='desc',
            new_name='jdesc',
        ),
    ]
