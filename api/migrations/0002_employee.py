# Generated by Django 3.0.5 on 2020-11-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
