# Generated by Django 4.2.4 on 2024-03-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_comment_user_id_alter_post_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="actual_comment",
            field=models.TextField(default=""),
        ),
    ]
