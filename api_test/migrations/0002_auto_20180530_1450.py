# Generated by Django 2.0.2 on 2018-05-30 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationreportsendconfig',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
    ]
