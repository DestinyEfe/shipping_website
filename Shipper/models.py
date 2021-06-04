from random import randint
import secrets, string

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

import barcode
from barcode.writer import ImageWriter
from io import BytesIO

COUNTRY_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

# Create your models here.
class Sender(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, default=0)
    country_code = models.CharField(max_length=4, default='+')
    postal_code = models.BigIntegerField(default=0)
    
    def __str__(self):
        return f'{self.name}'

class Receiver(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20, default=0)
    country_code = models.CharField(max_length=4, default='+')
    postal_code = models.BigIntegerField(default=0)


    def __str__(self):
        return self.name

class Package(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Receiver, on_delete=models.RESTRICT)
    packageId = models.IntegerField(default=randint(1111, 9999))
    package_name = models.CharField(max_length=500)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    tracking_code = models.CharField(
        max_length=25,
        default=f'DEST{randint(111111111111111, 999999999999999)}-CARGO'
    )
    barcode = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(max_length=7, default='pending')
    carrier = models.CharField(max_length=50, default='DHL')
    type_of_shipment = models.CharField(max_length=50, default='Air Freight')
    carrier_reference_no = models.CharField(max_length=200, default=f'HM1H{randint(1111, 9999)}')
    payment_mode = models.CharField(max_length=200, default='CASH')
    comments = models.CharField(max_length=100, default="Package won't be released for shipment until the shipment fees is being paid")
    expected_delivery_date = models.DateField()
    departure_time = models.TimeField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    piece_type = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50, default='')
    total_volume_weight = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    toal_actual_weight = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.package_name

    # def random_string(self):
    #     num = 10
    #     res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    #     return res +""+ '.png'

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{self.tracking_code}', writer=ImageWriter()) #generate barcode format of tracking_code
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


#for Package.tracking_code in line 44
#I used CharField instead of the BigIntegerField 
# because of the DESTI am appending at the front.

#Sender.packages_set.all()