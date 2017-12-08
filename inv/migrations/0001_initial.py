# Generated by Django 2.0 on 2017-12-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('number', models.CharField(max_length=50)),
                ('spinning_mill', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LCItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=20)),
                ('composition', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('unit', models.CharField(choices=[('kg', 'KG')], default='kg', max_length=2)),
                ('style_no', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=100)),
                ('rcv', models.PositiveIntegerField(default=0)),
                ('dlv', models.PositiveIntegerField(default=0)),
                ('lc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.LC')),
            ],
        ),
        migrations.CreateModel(
            name='YarnRcv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('challan_no', models.CharField(max_length=20)),
                ('lot', models.CharField(max_length=20)),
                ('quantity_rcv', models.PositiveIntegerField(verbose_name='Quantity Received')),
                ('lc_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.LCItem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]