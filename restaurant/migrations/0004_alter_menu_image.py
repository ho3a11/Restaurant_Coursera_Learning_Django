# Generated by Django 4.2.2 on 2023-06-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='menu_item/default_image.jpg', upload_to='menu_item/'),
        ),
    ]
