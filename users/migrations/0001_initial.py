# Generated by Django 4.0.5 on 2022-07-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('username', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('locations', models.ManyToManyField(to='locations.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
        ),
    ]
