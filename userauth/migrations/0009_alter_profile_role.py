# Generated by Django 5.1.3 on 2024-12-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0008_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient')], max_length=10),
        ),
    ]
