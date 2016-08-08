#!/usr/bin/env python
# Taylor Curley - 2016 - taylorcurley.co

from twython import Twython
from pyshorteners import Shortener
from secret_cpb import c_key, cs_key, a_token, as_token, google_api
from scrape import journal,title,url

api = Twython(c_key, cs_key, a_token, as_token)

api_key = google_api
shortener = Shortener('Google', api_key=api_key)
for i in title:
    link = format(shortener.short(url[i]))
    if len(str(title[i])) > 70:
        tweet = 'New from ' + journal[i] + ': "' + str(title[i][:70]) + '..." ' + '\n' + link
        api.update_status(status=tweet)
    else:
        tweet = 'New from ' + journal[i] + ': "' + str(title[i]) + '" ' + '\n' + link
        api.update_status(status=tweet)
     

