# Generated by Django 4.2.7 on 2023-11-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiftbooker', '0005_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='duh', upload_to=''),
            preserve_default=False,
        ),
    ]
