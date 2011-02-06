# GEOIP-REDIRECT Middleware & Decorators

## A django app to redirect based on an ip lookup

### Installation
Installing this is pretty simple - add the middleware and then configure it as
you need. You can test it by giving it an IP to *always* return regardless
of the user's current REMOTE_ADDR value. You can either enable the middleware
to process *all* views or alternativly import `geoip_redirect` and add
it as a decorator to your particular view(s).

To activate the middleware add:

    'geoip.middleware.GeoIPMiddleWare',

To your MIDDLEWARE_CLASSES tuple and *geoip* to your INSTALLED_APPS. To use
it on a view instead then do the following:

    from geoip.decorators import geoip_redirect
    
    @geoip_redirect
    def my_view(request):
        return HttpResponse('test')

### Configuration & Usage

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

If you only want the redirect to appear when a user lands on the homepage (in this
case a *request.path* matching "/") then set **HOMEPAGE_ONLY** to *True*. This
will force the middleware to return the normal response when other sub-urls
are accessed.

For now if you want that "remember choice" checkbox to work you need to hook in
a url to your conf:

    # handle save target redirect cookie
    (r'geoip/savetarget/', 'geoip.views.save_target'),

This part also reliies on jQuery being present to do the POST submit via ajax.

### Ip Lookup Data source

Database via: [maxmind](http://www.maxmind.com/app/geoip_country)

You can force in a "blank" field to be populated via the autoincrement with awk:

    awk '{print ","$0}' geo.csv  > geo2.csv

And then load in via a CSV import

    LOAD DATA LOCAL INFILE "geo2.csv" INTO TABLE geoip_geoiprecord
    FIELDS TERMINATED BY ',' ENCLOSED BY '"';

### Notes

You should be aware that within this the UK is set as *GB* when you add an "ip
redirect entry".

### Finally

I work at [udox](http://www.u-dox.com). We have lots more django code available
at our [github page](http://www.github.com/udox) that you might find useful. You
can find more about me at [jaymz.eu](http://jaymz.eu).