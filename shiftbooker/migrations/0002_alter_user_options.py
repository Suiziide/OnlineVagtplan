# Generated by Django 4.2.7 on 2023-11-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shiftbooker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_view_users_shifts', 'Can view users and shifts'),), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
