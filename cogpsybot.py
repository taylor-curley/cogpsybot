#!/usr/bin/env python
# Taylor Curley - 2016 - taylorcurley.co

from twython import Twython
from pyshorteners import Shortener
import datetime
from secret_cpb import c_key, cs_key, a_token, as_token, google_api
from scrape import journal,title,url

time = datetime.datetime.now()

api = Twython(c_key, cs_key, a_token, as_token)
api_key = google_api
shortener = Shortener('Google', api_key=api_key)

for i in title:
    link = format(shortener.short(url[i]))
    print('Tweeting out: "' + str(title) + '" at ' + str(time)) # Mirror in console
    if len(str(title[i])) > 65:
        tweet = 'From ' + journal[i] + ': "' + str(title[i][:65]) + '..." ' + '\n' + link
        api.update_status(status=tweet)
    else:
        tweet = 'From ' + journal[i] + ': "' + str(title[i]) + '" ' + '\n' + link
        api.update_status(status=tweet)
     

# Log posts
t = open('/home/taylor/Documents/bots/cpb_log.txt', 'a+')
t.write(str(time) + '  # of tweets: ' + str(len(title)) + '\n')
t.close()
