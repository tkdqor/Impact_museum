# Generated by Django 3.2.9 on 2022-05-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_post_top_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='short_content',
            field=models.CharField(max_length=200),
        ),
    ]
