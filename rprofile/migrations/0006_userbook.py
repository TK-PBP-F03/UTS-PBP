# Generated by Django 4.2.4 on 2023-10-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_count_read'),
        ('rprofile', '0005_alter_userprofile_email_alter_userprofile_handphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_count', models.PositiveIntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rprofile.userprofile')),
            ],
        ),
    ]