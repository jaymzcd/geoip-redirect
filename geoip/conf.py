from django.conf import settings as core_settings
from geoip import settings as geo_settings

def geo_setting(conf_var):
    """ Tries returning a value from the main settings file
    or the defaults in geoip/settings.py or ultimately None """

    try:
        return getattr(core_settings, conf_var)
    except AttributeError:
        try:
            return getattr(geo_settings, conf_var)
        except AttributeError:
            return None
