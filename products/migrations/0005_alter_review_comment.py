# Generated by Django 4.2.10 on 2024-05-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rating_review_delete_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
