# Generated by Django 3.0.6 on 2020-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_issue_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='issue_title',
            field=models.CharField(default='Issue', max_length=255),
        ),
    ]
