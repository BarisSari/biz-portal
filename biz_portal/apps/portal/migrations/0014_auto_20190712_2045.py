# Generated by Django 2.2.2 on 2019-07-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("portal", "0013_auto_20190712_1636")]

    operations = [
        migrations.AlterField(
            model_name="municipality",
            name="logo",
            field=models.CharField(
                blank=True, help_text="e.g. images/logo-WC033.png", max_length=200
            ),
        )
    ]
