# Generated by Django 4.2.4 on 2024-01-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_quiz_video_link_quiz_slides'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitting',
            name='user_attempt',
            field=models.IntegerField(default=1, verbose_name='Attempt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slides',
            field=models.TextField(blank=True, help_text='Copy the Embed link', null=True, verbose_name='Slides Link'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='current_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Current Score'),
        ),
    ]
