#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 17:54:35 2020

@author: fardeenmeeran
"""

import sports 
import csv



class sport:
   name = ""
   matchList = []
   processedMatches= []
   teamoneList = []
   teamtwoList = []


def scraper(sport,listi,matche,team1,team2):
    m = 0
    
    
  

    
    matches = sports.get_sport(sport)
  
    stry = str (matches)
    stry = stry.split(",")  
   
    for i in stry :
        if "0-0" in i :
            listi.append(i)
       
            matche = str(listi).split("-")

   
    for i in matche:
        
        if m % 2 == 0 :
            
            team1.append(i)
        elif m % 2 != 0 :
            team2.append(i)
        m = m +1 
    
 

basket = sport()
basket.name = "basketball"
scraper (sports.BASKETBALL,basket.matchList,basket.processedMatches,basket.teamoneList,basket.teamtwoList)
print(basket.matchList)

    






