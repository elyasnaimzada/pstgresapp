from django.db import models

# Create your models here.


class Jobs(models.Model):
    invoiceno = models.CharField(max_length=200)
    transtype = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    ticket = models.CharField(max_length=200)
    externalno = models.CharField(max_length=200)
    cctname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sordescription = models.TextField(max_length=None)
    qty = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)
    gst = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    notes = models.TextField(max_length=None, null=True)
    status = models.BooleanField("Charge valid", null=True)
    reversed = models.BooleanField(" Reversed", null=True)

    def __str__(self):
        return self.location
