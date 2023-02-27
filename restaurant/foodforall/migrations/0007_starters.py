# Generated by Django 4.1.7 on 2023-02-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodforall', '0006_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='starters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='img')),
                ('starter_name', models.CharField(max_length=20)),
                ('starter_desc', models.CharField(max_length=50)),
                ('starter_price', models.IntegerField()),
            ],
        ),
    ]
