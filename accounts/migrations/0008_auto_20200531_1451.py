# Generated by Django 3.0.6 on 2020-05-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200531_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]
