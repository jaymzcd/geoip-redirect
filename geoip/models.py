from django.db import models
from geoip.exceptions import NoGeoIPException, InvalidDottedIP

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

    @staticmethod
    def get_code(input_ip):
        """ Takes a string IP address and returns the country code if it could
        find one for it """
        
        return None

    @staticmethod
    def to_decimal(ip_str):
        """ Returns the decimal version of a dotted IP address """
        mults = [256**3, 256**2, 256**1, 256**0]
        chunks = ip_str.split('.')
        if(len(chunks)==4):
            return sum([int(chunks[x])*mults[x] for x in range(0,4)])
        else:
            raise InvalidDottedIP('Could not convert to decimal')
