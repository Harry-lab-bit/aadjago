# Generated by Django 4.2 on 2024-12-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0003_alter_contact_description_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('authname', models.CharField(max_length=15)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('tiemStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]