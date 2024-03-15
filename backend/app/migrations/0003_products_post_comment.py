# Generated by Django 4.2.4 on 2024-03-15 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_friends_friendmessage_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.IntegerField()),
                ("product_image", models.ImageField(upload_to="images/")),
                ("product_description", models.CharField(max_length=1000)),
                ("product_category", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default.jpg", null=True, upload_to=""
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("comment_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.post"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.users"
                    ),
                ),
            ],
        ),
    ]
