# Generated by Django 5.1.4 on 2024-12-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('email', models.EmailField()),
                ('msg', models.TextField(blank=True, default='text', null=True)),
            ],
        ),
    ]
