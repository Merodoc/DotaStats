#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:44:15 2019

@author: merodoc
"""

import csv
import numpy as np
import pandas as pd

Stats = []
with open('TI9.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar='|')
    for row in spamreader:
        Stats.append(row)
        
Team1 = []
Team2 = []
Winner = []
i = 0
for game in Stats:
    if i == 0:
        i += 1
    else:
        Team1.append(Stats[i][1])
        Team2.append(Stats[i][4])
        Winner.append(Stats[i][7])
        i += 1       
    
Teamlist = ['OG','Team Liquid', 'PSG.LGD','Team Secret','Vici Gaming','Evil Geniuses','Royal Never Give Up','Infamous Gaming', 'Newbee', 'TNC Predator','Virtus.pro','Fnatic','Alliance','Mineski','Natus Vincere', 'Chaos Esports Club', 'KEEN GAMING', 'Ninjas in Pyjamas']


wij = np.zeros((len(Teamlist), len(Teamlist)))


wincounts = []
for x in Teamlist:
    print(x)
    wincounts.append(Winner.count(x))


d = {'Radiant':Team1, 'Dire':Team2, 'Winner':Winner}

index_dict = {'OG':0,'Team Liquid':1,'PSG.LGD':2,'Team Secret':3,'Vici Gaming':4,'Evil Geniuses':5,'Royal Never Give Up':6,'Infamous Gaming':7,'Newbee':8,'TNC Predator':9,'Virtus.pro':10,'Fnatic':11,'Alliance':12,'Mineski':13,'Natus Vincere':14,'Chaos Esports Club':15,'KEEN GAMING':16,'Ninjas in Pyjamas':17}

games = pd.DataFrame(data = d)

Wi = pd.DataFrame(np.array([wincounts]), columns = Teamlist)
    
np.array(wincounts)
print(Wi)
print(games)
print(games.loc[:,'Radiant'])


for n in range(len(games.loc[:,'Radiant'])):
    i = games.loc[n,'Radiant']
    j = games.loc[n,'Dire']
    if games.loc[n,'Winner'] == i:
        wij[index_dict[i],index_dict[j]] += 1
    else:
        wij[index_dict[j],index_dict[i]] += 1

print(wij)
