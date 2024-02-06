# Generated by Django 5.0 on 2024-01-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_remove_user_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('FIRST', '1st year'), ('SECOND', '2nd year'), ('THIRD', '3rd year'), ('FORTH', '4th year'), ('FIFTH', '5th year')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
