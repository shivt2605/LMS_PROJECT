# Generated by Django 3.2 on 2023-06-17 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_course_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
