# Generated by Django 3.0 on 2021-06-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210629_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='comedy', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
