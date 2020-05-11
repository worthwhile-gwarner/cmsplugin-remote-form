# Generated by Django 2.2.12 on 2020-05-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_remote_form', '0006_auto_20200504_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remoteform',
            name='link_parameter',
            field=models.CharField(blank=True, default='', help_text='Adds a custom parameter onto the thanks page link', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='remoteform',
            name='post_url',
            field=models.CharField(blank=True, default='', help_text='Post form data to remote endpoint', max_length=200, null=True, verbose_name='Remote URL'),
        ),
        migrations.AlterField(
            model_name='remoteform',
            name='thanks',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Message displayed after submitting the contact form.'),
        ),
    ]
