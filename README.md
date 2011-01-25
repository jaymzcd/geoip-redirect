# geoip-redirect

## A django app to redirect based on an ip lookup

### Installation
Installing this is pretty simple - add the middleware and then configure it as
you need. You can test it by giving it an IP to *always* return regardless
of the user's current REMOTE_ADDR value.

Add:

    'geoip.middleware.GeoIPMiddleWare',

To your MIDDLEWARE_CLASSES tuple and *geoip* to your INSTALLED_APPS.

### Usage

You have 2 options - you can enable **REDIRECT_ALL** in the geoip settings
file & supply a list of codes or you can add admin entries with custom text
and domains per country code.

So if you want to just redirect France, Great Britain and Germany and you
don't want to have different targets for each you could just set **REDIRECT_ALL**
to *True* and then set **REDIRECT_CODES** to *['GB', 'FR', 'DE']*. Alternativly
you can add set it to *False* and add entries to the admin within *Ip
Redirect Entry*.

You can avoid handling particular URLs on the site by adding them to the
IgnoreURL patterns and settings **PROCESS_IGNORES** to *True* in settings. This
will do a lookup when the middleware starts and cache a list of URLs to ignore.
These are simply CharFields for now.

### Ip Lookup Data source

Database via: http://www.maxmind.com/app/geoip_country

You can force in a "blank" field to be populated via the autoincrement with awk:

    awk '{print ","$0}' geo.csv  > geo2.csv

And then load in via a CSV import

    LOAD DATA LOCAL INFILE "geo2.csv" INTO TABLE geoip_geoiprecord
    FIELDS TERMINATED BY ',' ENCLOSED BY '"';

### Notes

You should be aware that within this the UK is set as *GB* when you add an "ip
redirect entry".