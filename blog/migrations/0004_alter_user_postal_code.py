# Generated by Django 3.2.5 on 2021-07-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Postal_Code',
            field=models.IntegerField(null=True),
        ),
    ]