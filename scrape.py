# -*- coding: utf-8 -*-

import urllib.request
import datetime
from bs4 import BeautifulSoup

# Get date and time for log
time = datetime.datetime.now()

# Elsevier journal websites
journal_web = [
'http://www.journals.elsevier.com/cognitive-psychology/recent-articles', 
'http://www.journals.elsevier.com/acta-psychologica/recent-articles', 
'http://www.journals.elsevier.com/brain-and-cognition/recent-articles', 
'http://www.journals.elsevier.com/cognition/recent-articles', 
'http://www.journals.elsevier.com/consciousness-and-cognition/recent-articles', 
'http://www.journals.elsevier.com/journal-of-memory-and-language/recent-articles', 
'http://www.journals.elsevier.com/neuropsychologia/recent-articles', 
'http://www.journals.elsevier.com/trends-in-cognitive-sciences/recent-articles'
]

journal_title = [
"Cognitive Psychology", 
"Acta Psychologica",
"Brain and Cognition", 
"Cognition", 
"Consciousness and Cognition",
"Journal of Memory and Language", 
"Neuropsychologica", 
"Trends in Cognitive Sciences"
]

title = {}
url = {}
journal = {}

y = 0
for x in journal_web:
    # Read site
    o = urllib.request.urlopen(journal_web[y])
    site = BeautifulSoup(o, "lxml")
    
    # Pull 3 most current postings (rawish data)
    titleOne = site.find_all("div", class_="pod-listing-header", limit=3)
    titleOne = BeautifulSoup(str(titleOne), 'html.parser')
    titleTwo = titleOne.find_all("a", title=True)
    
    # Keep track of published articles
    title = {}
    url = {}
    f = open('tweeted_pubs.txt', 'a+')
    g = open('tweeted_pubs.txt', 'r')
    g = [line.rstrip('\n') for line in g]
    
    for i in range(3):
        entry = titleTwo[i]['title']
        if entry in g:
            print('Redundant entry... ' + str(time))
        else:
            title[i] = titleTwo[i]['title']
            url[i] = titleTwo[i]['href']
            journal[i] = str(journal_title[y])
            # Log article names + URLs 
            f.write(str(entry) + '\n' + str(url[i]) + '\n')  
            # Mirror on command prompt
            print('Tweeting out: "' + str(entry) + '" at ' + str(time))  
    f.close()
    y = y + 1

