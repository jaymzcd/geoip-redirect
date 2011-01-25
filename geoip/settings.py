REDIRECT_ALL = True # if false then only handle for those with a IPRedirectEntry
REDIRECT_DOMAIN = 'http://www.google.com' # The domain to redirect to if REDIRECT_ALL is True
REDIRECT_CODES = ['GB', 'FR', 'DE']

FAIL_ON_MISSING = False # If we want to raise Exceptions when no code was found
SHOW_FOR_MISSING = True # If true then we should pop up an option anyway
MISSING_DOMAIN = 'http://www.vans.com/intl/' # Target URL when we have no idea where they are

PROCESS_IGNORES = True # Whether to make a db hit to grab the url ignore list (on middleware __init__)

DEBUG_IP = '92.52.69.82' # Set this if you want to force it to "find" this particular address
