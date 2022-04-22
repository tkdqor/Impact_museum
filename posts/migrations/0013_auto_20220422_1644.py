# Generated by Django 3.2.9 on 2022-04-22 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220404_1420'),
        ('posts', '0012_problem_short_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('NORMAL', '일반'), ('DISABLED', '장애인'), ('ENVIRONMENT', '환경'), ('EMPLOYMENT', '고용'), ('EDUCATION', '교육'), ('ELDERS', '노인')], default='NORMAL', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]
