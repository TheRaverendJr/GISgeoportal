# Generated by Django 4.1.2 on 2022-11-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='area',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='cctv',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='elevator',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='furnished',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='parking',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='rental_frequency',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='rooms',
        ),
        migrations.AddField(
            model_name='listing',
            name='parish',
            field=models.CharField(blank=True, choices=[('Mathews Cathedral Archdeaconry', 'Mathews Cathedral Archdeaconry'), ('Emmanuel Archdeaconry', 'Emmanuel Archdeaconry')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.CharField(choices=[('Cathedral', 'Cathedral'), ('Church', 'Church'), ('Office', 'Office')], max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='property_status',
            field=models.CharField(blank=True, choices=[('Registered', 'Registered'), ('Unregistered', 'Unregistered')], max_length=20, null=True),
        ),
    ]