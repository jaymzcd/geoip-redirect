from django.db import models
from django.conf import settings
from geoip.conf import geo_setting
from geoip.exceptions import NoGeoIPException, InvalidDottedIP

class GeoIPRecord(models.Model):
    """ The source data for this table can be found at
    http://www.maxmind.com/app/geoip_country. Fields are as they are from
    that file so load in via the process in the README """

    start_ip = models.IPAddressField()
    end_ip = models.IPAddressField()
    start_decimal = models.BigIntegerField()
    end_decimal = models.BigIntegerField()
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=25)

    def __unicode__(self):
        return '%s - %s [%s]' % (self.start_ip, self.end_ip, self.country_code)

    @staticmethod
    def get_code(input_ip):
        """ Takes a string IP address and returns the country code if it could
        find one for it """

        try:
            input_decimal = GeoIPRecord.to_decimal(input_ip)
        except InvalidDottedIP:
            raise InvalidDottedIP

        bounds = GeoIPRecord.objects.filter(start_decimal__lte=input_decimal,
            end_decimal__gte=input_decimal)

        # In theory we should only have 1 record here
        try:
            return bounds[0].country_code
        except IndexError:
            if settings.DEBUG and geo_setting('FAIL_ON_MISSING'):
                raise NoGeoIPException
            else:
                pass

    @staticmethod
    def to_decimal(ip_str):
        """ Returns the decimal version of a dotted IP address """

        mults = [256**3, 256**2, 256**1, 256**0]
        chunks = ip_str.split('.')
        if(len(chunks)==4):
            return sum([int(chunks[x])*mults[x] for x in range(0,4)])
        else:
            if settings.DEBUG:
                raise InvalidDottedIP('Could not convert to decimal')
            else:
                pass

class IPRedirectEntry(models.Model):
    """ This model is used to admin the active redirects for the middleware """

    incoming_country_code = models.CharField(max_length=2, unique=True)
    target_domain = models.URLField(verify_exists=False)
    custom_message = models.TextField(blank=True, null=True)
    custom_image = models.ImageField(upload_to='uploads/geoip/', blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.incoming_country_code, self.target_domain)

    def save(self):
        # Force the country code to always be uppercase to match the
        # db data that we have imported
        self.incoming_country_code = self.incoming_country_code.upper()
        super(IPRedirectEntry, self).save()

    class Meta:
        ordering = ('incoming_country_code',)

class IgnoreURL(models.Model):
    """ Url paths to ignore from showing a redirect on """

    url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.url

