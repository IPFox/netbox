# Generated by Django 3.1 on 2020-12-02 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0052_customfield_cleanup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webhook',
            old_name='obj_type',
            new_name='content_types',
        ),
    ]
