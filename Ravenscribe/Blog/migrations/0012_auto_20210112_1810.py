# Generated by Django 3.1.3 on 2021-01-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]