# Generated by Django 4.1.6 on 2023-02-24 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_demo_model', '0018_branch_data_delete_bio_delete_chemi_delete_dssi_and_more'),
        ('app_prediction', '0011_alter_userpredict_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpredict',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_demo_model.branch'),
        ),
        migrations.AlterField(
            model_name='userpredict',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
