# Generated by Django 3.2.16 on 2022-11-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_music', '0004_alter_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='../static/image/spotiflix.jpg', upload_to='django-image/'),
        ),
    ]
