#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import datetime
from bs4 import BeautifulSoup

# Get date and time for log
time = datetime.datetime.now()

# Elsevier journal websites
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

title = {}
url = {}
journal = {}

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
            title[i] = titleTwo[i]['title']
            url[i] = titleTwo[i]['href']
            journal[i] = str(ejournal_title[y])
            # Log article names + URLs 
            f.write(str(entry) + '\n' + str(url[i]) + '\n')  
              
    f.close()
    y = y + 1

