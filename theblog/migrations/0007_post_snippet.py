# Generated by Django 3.2.5 on 2021-07-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link above to view the blog', max_length=255),
        ),
    ]
