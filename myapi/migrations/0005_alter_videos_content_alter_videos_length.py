# Generated by Django 4.0.6 on 2022-07-23 04:47

from django.db import migrations, models
import myapi.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_videos_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='content',
            field=models.FileField(upload_to='', validators=[myapi.validators.validate_file_size, myapi.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='videos',
            name='length',
            field=models.PositiveBigIntegerField(null=True, validators=[myapi.validators.validate_length]),
        ),
    ]
