# Generated by Django 4.1.7 on 2023-10-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
