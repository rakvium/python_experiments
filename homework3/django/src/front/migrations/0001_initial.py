# Generated by Django 2.0.6 on 2018-07-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
