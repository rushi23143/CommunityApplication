# Generated by Django 3.1.5 on 2021-03-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
