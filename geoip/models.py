from django.db import models

class GeoIPRecord(models.Model):
    """ The source data for this table can be found at
    http://www.maxmind.com/app/geoip_country. Fields are as they are from
    that file so load in via the process in the README """

    start_ip = models.IPAddressField()
    end_ip = models.IPAddressField()
    start_decimal = models.IntegerField()
    end_decimal = models.IntegerField()
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s - %s [%s]' % (self.start_ip, self.end_ip, self.country_code)

