# Generated by Django 3.1.7 on 2021-02-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0003_auto_20210228_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevent',
            name='image',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
