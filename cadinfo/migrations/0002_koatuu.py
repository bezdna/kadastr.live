# Generated by Django 3.1.4 on 2020-12-06 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koatuu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koatuu_id', models.CharField(max_length=32)),
                ('name', models.TextField()),
                ('type', models.CharField(max_length=2)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadinfo.koatuu')),
            ],
        ),
    ]