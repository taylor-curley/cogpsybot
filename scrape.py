#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import datetime
import feedparser
import datetime
from bs4 import BeautifulSoup

# Get date and time for log
time = datetime.datetime.now()

################################################################################
# Elsevier journal websites #
ejournal_web = [
'http://www.journals.elsevier.com/cognitive-psychology/recent-articles', 
'http://www.journals.elsevier.com/acta-psychologica/recent-articles', 
'http://www.journals.elsevier.com/brain-and-cognition/recent-articles', 
'http://www.journals.elsevier.com/cognition/recent-articles', 
'http://www.journals.elsevier.com/consciousness-and-cognition/recent-articles', 
'http://www.journals.elsevier.com/journal-of-memory-and-language/recent-articles', 
'http://www.journals.elsevier.com/neuropsychologia/recent-articles', 
'http://www.journals.elsevier.com/trends-in-cognitive-sciences/recent-articles', 
'http://www.journals.elsevier.com/journal-of-applied-research-in-memory-and-cognition/recent-articles'
]

# Elsevier journal titles (cannot exceed 50 characters)
ejournal_title = [
"Cognitive Psychology", 
"Acta Psychologica",
"Brain and Cognition", 
"Cognition", 
"Consciousness and Cognition",
"Journal of Memory and Language", 
"Neuropsychologica", 
"Trends in Cognitive Sciences", 
"Applied Research in Memory & Cognition"
]

etitle = []
eurl = []
ejournal = []

# Loop through Elsevier journals
y = 0
for x in ejournal_web:
    # Read site
    o = urllib.request.urlopen(ejournal_web[y])
    site = BeautifulSoup(o, "lxml")
    
    # Pull 3 most current postings (rawish data)
    titleOne = site.find_all("div", class_="pod-listing-header", limit=3)
    titleOne = BeautifulSoup(str(titleOne), 'html.parser')
    titleTwo = titleOne.find_all("a", title=True)
    
    # Keep track of published articles
    f = open('/home/taylor/Documents/bots/tweeted_pubs.txt', 'a+')
    g = open('/home/taylor/Documents/bots/tweeted_pubs.txt', 'r')
    g = [line.rstrip('\n') for line in g]
    
    for i in range(3):
        entry = titleTwo[i]['title']
        if entry in g:
            print('Redundant entry... ' + str(time))
        else:
            etitle.append(titleTwo[i]['title'])
            eurl.append(titleTwo[i]['href'])
            ejournal.append(str(ejournal_title[y]))
            # Log article names + URLs 
            f.write(str(entry) + '\n' + str(titleTwo[i]['href']) + '\n')  
              
    f.close()
    y = y + 1


################################################################################
# Springer and T&F journal websites

sjournal_web = [
"http://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=40631&channel-name=Bulletin+of+the+Psychonomic+Society.rss", 
"http://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=13421&channel-name=Memory+%26+Cognition.rss", 
"http://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=13420&channel-name=Learning+%26+Behavior.rss", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=pvis20", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=pcgn20", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=pmem20", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=pcgn20", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=plcp21", 
"http://tandfonline.com/action/showFeed?type=etoc&feed=rss&jc=pecp21"
]

sjournal_title = [
"Bulletin of the Psychonomic Society", 
"Memory & Cognition", 
"Learning & Behavior", 
"Visual Cognition", 
"Cognitive Neuropsychology", 
"Memory", 
"Cognitive Neuroscience", 
"Language, Cognition and Neuroscience", 
"Journal of Cognitive Psychology"
]

stitle = []
surl = []
sjournal = []

y = 0
for x in sjournal_web:
    # Read XML feed
    site = feedparser.parse(sjournal_web[y])

    # Keep track of published articles
    f = open('/home/taylor/Documents/bots/tweeted_pubs.txt', 'a+')
    g = open('/home/taylor/Documents/bots/tweeted_pubs.txt', 'r')
    g = [line.rstrip('\n') for line in g]

    for i in range(3):
        entry = site['entries'][i]['title']
        entry_url = site['entries'][i]['link']
        if entry in g:
            print('Redundant entry... ' + str(time))
        else:
            # Log article names + URLs 
            stitle.append(site['entries'][i]['title'])
            surl.append(site['entries'][i]['link'])
            sjournal.append(sjournal_title[y])
            f.write(str(entry) + '\n' + str(entry_url) + '\n') 
              
    f.close()
    y = y + 1
