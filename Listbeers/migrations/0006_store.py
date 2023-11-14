# Generated by Django 4.2.7 on 2023-11-14 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listbeers', '0005_remove_breweries_state_alter_beer_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('local', models.TextField()),
                ('beer', models.ManyToManyField(to='Listbeers.beer')),
            ],
        ),
    ]