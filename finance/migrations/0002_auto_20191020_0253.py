# Generated by Django 2.2.3 on 2019-10-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='movement',
            name='datePosted',
            field=models.DateField(),
        ),
    ]
