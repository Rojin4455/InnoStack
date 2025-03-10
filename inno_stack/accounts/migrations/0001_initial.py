# Generated by Django 5.1.6 on 2025-02-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField()),
                ('company_id', models.CharField(max_length=50)),
                ('location_id', models.CharField(max_length=50)),
                ('refresh_token', models.TextField()),
                ('scope', models.TextField()),
                ('token_type', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
                ('expires_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
