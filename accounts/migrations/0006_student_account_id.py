# Generated by Django 3.2.4 on 2023-10-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_visa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='account_id',
            field=models.PositiveBigIntegerField(null=True, unique_for_year=True),
        ),
    ]