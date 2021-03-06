import urllib.request as urllib2
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import pprint, requests, sys, os, re
from datetime import datetime, date

# Use this as url for cli but going to hardcode it for now
url = 'https://www.scorespro.com/'
url2 = 'https://www.scorespro.com/basketball/'
# url = str(sys.argv[1])

def soup_it(url):
    result = requests.get(url)
    src = result.content
    # page = requests.get(url, headers = headers)
    soup = BeautifulSoup(src, "lxml")
    return soup


def find_data(url):
    soup = soup_it(url)
    # Looks in at the mainfeed
    main_feed = soup.find('div', id="mainfeed")    
    # gets all the comp groups 
    comp_groups = main_feed.find_all('div', class_='compgrp')
    # Find Leauge Data in compgroups
    main_sports = []
    for leauge in comp_groups:
        
        leauge_name = ''
        kick_off_time = ''

        l_data = leauge.find(lambda tag: tag.name=='td', class_ ="blockBarLt")
        for a in l_data.find_all('a'):
            leauge_name += a.text
        
        matches_in_leauges = leauge.find_all('table', id = 'blocks')
        for match in matches_in_leauges:
            # KickOff Timings
            match_kick = str(match.find(lambda tag: tag.name=='td', class_ ="kick"))
            match_kick_str = re.sub('^<.$>',"", (match_kick))
            # Find the status 
            status_td = match.find(lambda tag: tag.name=='td', class_ ="status")
            status = status_td.find(lambda tag: tag.name == 'span')
            if status == None or len(status) == 0: 
                status = "None"
            else:
                status = status.text

            # Home Team
            home_uc = match.find(lambda tag: tag.name=='td', class_ ="home")
            home = home_uc.find(lambda tag: tag.name == 'a')
            if home == None or len(home) == 0: 
                home = "None"
            else:
                home = home.text

            # away Team
            away_uc = match.find(lambda tag: tag.name=='td', class_ ="away")
            away = away_uc.find(lambda tag: tag.name == 'a')
            if away == None or len(away) == 0: 
                away = "None"
            else:
                away = away.text

             # Score of both teams
            score_td = match.find(lambda tag: tag.name=='td', class_ ="score")
            score = score_td.find(lambda tag: tag.name == 'a')
            if score == None or len(score) == 0: 
                score = "0 - 0"
            else:
                score = score.text

            today = date.today()
            print(today)
            main_sports.append([leauge_name, home, score, away, match_kick_str])

    return main_sports
"""  
def find_data_basket(url):
    soup = soup_it(url)
    # Looks in at the mainfeed
    main_feed = soup.find('div', id="mainfeed")    
    # gets all the comp groups 
    comp_groups = main_feed.find_all('div', class_='compgrp')
    # Find Leauge Data in compgroups
    main_sports = []
  
    for leauge in comp_groups:
        
        leauge_name = ''
        kick_off_time = ''

        l_data = leauge.find(lambda tag: tag.name=='td', class_ ="blockBarLt")
        for a in l_data.find_all('a'):
            leauge_name += a.text
            print(leauge_name)
        
        matches_in_leauges = leauge.find_all('table')
        print(matches_in_leauges)
        for match in matches_in_leauges:
         match_kick = (match.find(lambda tag: tag.name=='td', class_ ="datetime"))
         match_kick.text
         
         
         """ 
       
         status_td = match.find(lambda tag: tag.name=='td', class_ ="status")
  
         if status_td != None:
            status = status_td.find(lambda tag: tag.name == 'span')
            status = status.text
         else:
             status = "NONE"
            
       
         if status == None: 
             status = "None"
         else:
      
          
             
         home_uc = match.find(lambda tag: tag.name=='td', class_ ="h_n hometown")
         home = home_uc.find(lambda tag: tag.name == 'a')
         if home == None or len(home) == 0: 
                home = "None"
         else:
                home = home.text       
         away_uc = match.find(lambda tag: tag.name=='td', class_ ="away")
         away = away_uc.find(lambda tag: tag.name == 'a')
         if away == None or len(away) == 0: 
                away = "None"
         else:
                away = away.text
         score_td = match.find(lambda tag: tag.name=='td', class_ ="total ts_set")
         score = score_td.find(lambda tag: tag.name == 'a')
         if score == None or len(score) == 0: 
                score = "0 - 0"
         else:
                score = score.text
         main_sports.append([leauge_name, home, score, away,match_kick])
    return main_sports 
"""        
      

print(find_data(url))
print(find_data_basket(url2))

