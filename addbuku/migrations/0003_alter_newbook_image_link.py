# Generated by Django 4.2.6 on 2023-10-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbuku', '0002_alter_newbook_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newbook',
            name='image_link',
            field=models.URLField(default='https://img.freepik.com/premium-vector/open-blank-book-illustration-school-supply-back-school-open-book-icon-reading-writing_502505-530.jpg?w=2000', max_length=300),
        ),
    ]