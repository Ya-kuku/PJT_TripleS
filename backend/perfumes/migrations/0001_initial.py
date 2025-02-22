# Generated by Django 2.2.16 on 2020-11-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField()),
                ('year', models.IntegerField(null=True)),
                ('gender', models.IntegerField()),
                ('state', models.IntegerField()),
                ('brand', models.CharField(max_length=300)),
                ('info', models.TextField(null=True)),
                ('top', models.TextField(null=True)),
                ('mid', models.TextField(null=True)),
                ('base', models.TextField(null=True)),
                ('line', models.TextField(null=True)),
            ],
        ),
    ]
