REDIRECT_ALL = True # if false then only handle for those with a IPRedirectEntry
REDIRECT_DOMAIN = 'http://www.google.com' # The domain to redirect to if REDIRECT_ALL is True
REDIRECT_CODES = ['GB', 'FR', 'DE']

FAIL_ON_MISSING = False # If we want to raise Exceptions when no code was found

DEBUG_IP = '62.149.188.154' # Set this if you want to force it to "find" this particular address