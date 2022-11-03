# Generated by Django 3.2.16 on 2022-10-30 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_music', '0006_album_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='artist_surname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_file',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='album',
            name='album_artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_artist',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='streaming_music.album'),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='streaming_music.artist'),
        ),
    ]