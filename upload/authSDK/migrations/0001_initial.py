# Generated by Django 4.0rc1 on 2021-12-03 13:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=255, unique=True)),
                ('jwt_secret', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'db_table': 'users_user',
                'managed': False,
            },
        ),
    ]
