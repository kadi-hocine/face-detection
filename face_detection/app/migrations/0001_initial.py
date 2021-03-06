# Generated by Django 3.2.5 on 2021-07-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('isBlackList', models.BooleanField()),
                ('gender', models.BooleanField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
