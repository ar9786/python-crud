# Generated by Django 3.0.5 on 2020-11-28 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201128_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_course_details', to='api.Course'),
        ),
    ]
