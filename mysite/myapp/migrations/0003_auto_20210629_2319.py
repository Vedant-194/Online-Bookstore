# Generated by Django 3.0 on 2021-06-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Mr. ABC', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='media/book_images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_pdf',
            field=models.FileField(default='default.pdf', upload_to='media/book_pdf'),
        ),
    ]