# Generated by Django 4.1.6 on 2023-02-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_post_content_post_likes_post_owner_post_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='LikedBy',
            field=models.JSONField(default=list),
        ),
    ]
