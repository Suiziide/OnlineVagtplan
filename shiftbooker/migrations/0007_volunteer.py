# Generated by Django 4.2.7 on 2023-11-17 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shiftbooker', '0006_alter_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
                ('phone', models.CharField(max_length=100)),
                ('shifts_taken', models.IntegerField(verbose_name='Number of shifts taken')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
