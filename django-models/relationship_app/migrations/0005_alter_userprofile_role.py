# Generated by Django 5.1.3 on 2024-11-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')], max_length=20),
        ),
    ]
