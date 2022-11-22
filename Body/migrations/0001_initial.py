# Generated by Django 3.2.15 on 2022-11-22 13:54

import Body.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('a1c', models.CharField(blank=True, max_length=20, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('systolic', models.FloatField(blank=True, null=True)),
                ('diastolic', models.FloatField(blank=True, null=True)),
                ('pulse', models.CharField(blank=True, max_length=20, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodSugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('sugar', models.FloatField(blank=True, null=True)),
                ('exercise', models.FloatField(blank=True, null=True)),
                ('drug', models.FloatField(blank=True, null=True)),
                ('timeperiod', models.IntegerField(blank=True, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('member_id', models.CharField(blank=True, max_length=20, null=True)),
                ('reply_id', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('meal', models.IntegerField(blank=True, null=True)),
                ('tag', Body.models.ListField(blank=True, max_length=200, null=True)),
                ('image', models.IntegerField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('type', models.BooleanField(blank=True, default=False, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('diabetes_type', models.IntegerField(blank=True, null=True)),
                ('oad', models.BooleanField(blank=True, default=False, null=True)),
                ('insulin', models.BooleanField(blank=True, default=False, null=True)),
                ('anti_hypertensives', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('sugar_delta_max', models.IntegerField(blank=True, null=True)),
                ('sugar_delta_min', models.IntegerField(blank=True, null=True)),
                ('sugar_morning_max', models.IntegerField(blank=True, null=True)),
                ('sugar_morning_min', models.IntegerField(blank=True, null=True)),
                ('sugar_evening_max', models.IntegerField(blank=True, null=True)),
                ('sugar_evening_min', models.IntegerField(blank=True, null=True)),
                ('sugar_before_max', models.IntegerField(blank=True, null=True)),
                ('sugar_before_min', models.IntegerField(blank=True, null=True)),
                ('sugar_after_max', models.IntegerField(blank=True, null=True)),
                ('sugar_after_min', models.IntegerField(blank=True, null=True)),
                ('systolic_max', models.IntegerField(blank=True, null=True)),
                ('systolic_min', models.IntegerField(blank=True, null=True)),
                ('diastolic_max', models.IntegerField(blank=True, null=True)),
                ('diastolic_min', models.IntegerField(blank=True, null=True)),
                ('pulse_max', models.IntegerField(blank=True, null=True)),
                ('pulse_min', models.IntegerField(blank=True, null=True)),
                ('weight_max', models.IntegerField(blank=True, null=True)),
                ('weight_min', models.IntegerField(blank=True, null=True)),
                ('bmi_max', models.IntegerField(blank=True, null=True)),
                ('bmi_min', models.IntegerField(blank=True, null=True)),
                ('body_fat_max', models.IntegerField(blank=True, null=True)),
                ('body_fat_min', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Userdefault',
            },
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('after_recording', models.BooleanField(blank=True, default=False, null=True)),
                ('no_recording_for_a_day', models.BooleanField(blank=True, default=False, null=True)),
                ('over_max_or_under_min', models.BooleanField(blank=True, default=False, null=True)),
                ('after_meal', models.BooleanField(blank=True, default=False, null=True)),
                ('unit_of_sugar', models.BooleanField(blank=True, default=False, null=True)),
                ('unit_of_weight', models.BooleanField(blank=True, default=False, null=True)),
                ('unit_of_height', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Usersetting',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('body_fat', models.FloatField(blank=True, null=True)),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('recorded_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
