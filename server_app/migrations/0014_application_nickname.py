# Generated by Django 4.1.3 on 2023-01-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0013_alter_users_clan_alter_users_data_alter_users_tier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='nickname',
            field=models.TextField(blank=True, verbose_name='Имя продавца'),
        ),
    ]
