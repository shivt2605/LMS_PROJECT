# Generated by Django 3.2 on 2023-06-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_course_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='certificate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
