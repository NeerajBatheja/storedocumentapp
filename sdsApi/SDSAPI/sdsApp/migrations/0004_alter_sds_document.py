# Generated by Django 3.2.9 on 2021-11-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdsApp', '0003_alter_sds_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sds',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]