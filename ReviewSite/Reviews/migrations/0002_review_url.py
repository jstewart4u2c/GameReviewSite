# Generated by Django 5.0.4 on 2024-04-20 21:22

import embed_video.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='url',
            field=embed_video.fields.EmbedVideoField(default='https://www.youtube.com/@juicyj4u2c/videos'),
        ),
    ]