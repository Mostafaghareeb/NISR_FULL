# Generated by Django 5.1.1 on 2024-10-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=11)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=50)),
            ],
        ),
    ]
