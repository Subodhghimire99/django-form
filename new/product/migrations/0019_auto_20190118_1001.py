# Generated by Django 2.0.7 on 2019-01-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20190117_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Email',
            field=models.EmailField(max_length=70),
        ),
    ]
