# geoip-redirect

## A django app to redirect based on an ip lookup

### Data source

Database via: http://www.maxmind.com/app/geoip_country

You can force in a "blank" field to be populated via the autoincrement with awk:

    awk '{print ","$0}' geo.csv  > geo2.csv

And then load in via a CSV import

    LOAD DATA LOCAL INFILE "geo2.csv" INTO TABLE geoip_geoiprecord
    FIELDS TERMINATED BY ',' ENCLOSED BY '"';

### Notes

You should be aware that within this the UK is set as *GB* when you add an "ip
redirect entry".