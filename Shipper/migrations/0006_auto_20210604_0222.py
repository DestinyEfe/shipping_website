# Generated by Django 3.2.4 on 2021-06-04 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipper', '0005_auto_20210604_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='package',
            name='piece_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='package',
            name='toal_actual_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='package',
            name='total_volume_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='carrier_reference_no',
            field=models.CharField(default='HM1H1686', max_length=200),
        ),
        migrations.AlterField(
            model_name='package',
            name='departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='expected_delivery_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='packageId',
            field=models.IntegerField(default=4797),
        ),
        migrations.AlterField(
            model_name='package',
            name='pick_up_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='pick_up_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='tracking_code',
            field=models.CharField(default='DEST358006122404910-CARGO', max_length=25),
        ),
    ]
