# Generated by Django 4.2.6 on 2023-10-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbuku', '0003_alter_newbook_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbook',
            name='votes',
            field=models.PositiveIntegerField(default=1),
        ),
    ]