# Generated by Django 5.1.4 on 2025-01-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_reviews_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_slide', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
