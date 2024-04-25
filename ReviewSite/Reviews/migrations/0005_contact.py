# Generated by Django 5.0.4 on 2024-04-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0004_alter_review_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]