# Generated by Django 2.1.3 on 2018-12-07 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('from_address', models.TextField()),
                ('to_address', models.TextField()),
                ('organization', models.CharField(max_length=50)),
                ('other_info', models.TextField()),
            ],
        ),
    ]
