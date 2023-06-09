# Generated by Django 4.1.6 on 2023-02-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo_model', '0013_alter_major_abbreviation_alter_major_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(default='', max_length=100)),
                ('admission_grade', models.CharField(max_length=20)),
                ('gpa_year_1', models.CharField(max_length=20)),
                ('thai', models.CharField(max_length=20)),
                ('math', models.CharField(max_length=20)),
                ('sci', models.CharField(max_length=20)),
                ('society', models.CharField(max_length=20)),
                ('hygiene', models.CharField(max_length=20)),
                ('art', models.CharField(max_length=20)),
                ('career', models.CharField(max_length=20)),
                ('langues', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CHEMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(default='', max_length=100)),
                ('admission_grade', models.CharField(max_length=20)),
                ('gpa_year_1', models.CharField(max_length=20)),
                ('thai', models.CharField(max_length=20)),
                ('math', models.CharField(max_length=20)),
                ('sci', models.CharField(max_length=20)),
                ('society', models.CharField(max_length=20)),
                ('hygiene', models.CharField(max_length=20)),
                ('art', models.CharField(max_length=20)),
                ('career', models.CharField(max_length=20)),
                ('langues', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DSSI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(default='', max_length=100)),
                ('admission_grade', models.CharField(max_length=20)),
                ('gpa_year_1', models.CharField(max_length=20)),
                ('thai', models.CharField(max_length=20)),
                ('math', models.CharField(max_length=20)),
                ('sci', models.CharField(max_length=20)),
                ('society', models.CharField(max_length=20)),
                ('hygiene', models.CharField(max_length=20)),
                ('art', models.CharField(max_length=20)),
                ('career', models.CharField(max_length=20)),
                ('langues', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ICT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(default='', max_length=100)),
                ('admission_grade', models.CharField(max_length=20)),
                ('gpa_year_1', models.CharField(max_length=20)),
                ('thai', models.CharField(max_length=20)),
                ('math', models.CharField(max_length=20)),
                ('sci', models.CharField(max_length=20)),
                ('society', models.CharField(max_length=20)),
                ('hygiene', models.CharField(max_length=20)),
                ('art', models.CharField(max_length=20)),
                ('career', models.CharField(max_length=20)),
                ('langues', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
