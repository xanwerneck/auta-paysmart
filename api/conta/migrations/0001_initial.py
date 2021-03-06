# Generated by Django 2.2.17 on 2020-12-13 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
        ('corretora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corretora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corretora.Corretora')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='ContaInvestimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conta.Conta')),
            ],
        ),
        migrations.CreateModel(
            name='TipoInvestimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_investido', models.FloatField()),
                ('conta_investimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conta.ContaInvestimento')),
                ('tipo_investimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conta.TipoInvestimento')),
            ],
        ),
        migrations.CreateModel(
            name='ContaCorrente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.FloatField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conta.Conta')),
            ],
        ),
    ]
