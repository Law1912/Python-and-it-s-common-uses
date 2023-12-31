# Generated by Django 4.0.6 on 2022-08-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('research_interests', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
