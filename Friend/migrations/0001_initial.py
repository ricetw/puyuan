# Generated by Django 3.2.15 on 2022-11-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendsend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('relation_id', models.CharField(max_length=20)),
                ('type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('profile_id', models.IntegerField(blank=True, null=True)),
                ('relation_type', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
