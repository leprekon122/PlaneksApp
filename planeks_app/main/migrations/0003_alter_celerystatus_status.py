# Generated by Django 4.0.3 on 2022-03-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_celerystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerystatus',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]