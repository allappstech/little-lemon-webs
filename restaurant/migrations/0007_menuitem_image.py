# Generated by Django 4.2.1 on 2023-06-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_user_email_alter_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=False, null=True, upload_to='menu_images'),
        ),
    ]
