# Generated by Django 3.1.2 on 2023-01-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
    ]
