# Generated by Django 2.2.17 on 2020-12-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integradora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=255)),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]