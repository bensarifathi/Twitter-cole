# Generated by Django 3.1.7 on 2021-04-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isVerified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
