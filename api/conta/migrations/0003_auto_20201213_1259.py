# Generated by Django 2.2.17 on 2020-12-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0002_auto_20201213_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conta',
            old_name='card_id',
            new_name='account_id_paysmart',
        ),
    ]
