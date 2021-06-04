# Generated by Django 3.2.4 on 2021-06-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipper', '0007_auto_20210604_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='package',
            name='carrier_reference_no',
            field=models.CharField(default='HM1H5880', max_length=200),
        ),
        migrations.AlterField(
            model_name='package',
            name='packageId',
            field=models.IntegerField(default=1232),
        ),
        migrations.AlterField(
            model_name='package',
            name='tracking_code',
            field=models.CharField(default='DEST735311204827879-CARGO', max_length=25),
        ),
    ]
