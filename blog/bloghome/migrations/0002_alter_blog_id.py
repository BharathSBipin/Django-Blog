# Generated by Django 5.0.6 on 2024-06-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloghome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]