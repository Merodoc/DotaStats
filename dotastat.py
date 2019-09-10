#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:44:15 2019

@author: merodoc
"""

import csv


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
    Team1.append(Stats[i][1])
    Team2.append(Stats[i][4])
    Winner.append(Stats[i][7])
    i += 1
    
Teamlist = ['OG','Team Liquid', 'PSG.LGD','Team Secret','Vici Gaming','Evil Geniuses','Royal Never Give Up','Infamous Gaming', 'Newbee', 'TNC Predator','Virtus.pro','Fnatic','Alliance','Mineski','Natus Vincere', 'Chaos Esports Club', 'Keen Gaming', 'Ninjas in Pyjamas']