# Generated by Django 2.0.1 on 2019-09-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_paragraph', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
