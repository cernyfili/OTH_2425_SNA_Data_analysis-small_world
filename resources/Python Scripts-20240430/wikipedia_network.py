# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 23:48:36 2022

@author: 451966
"""

import wikipediaapi
import csv
import re

def read_file(file):
    with open(file,encoding='UTF-8',newline='') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def get_links(page):
    links = page.links
    filtered_links = []
    for title in links.keys():
        if title.find("Help")==-1 and title.find("Category")==-1 and title.find("Template")==-1 and title.find("Wikipedia")==-1 and page.text.find(title)!=-1:
            filtered_links.append(title)
    return filtered_links


# name of files and path has to be modified based on the name and location on your machine    
# files with the list of pages used to form the network
file = 'data/world_countries.txt'

#output file (edge list)
file_out = "data/wolrd_countries_net.csv"
lines = read_file(file)
file_net = open(file_out, 'w', encoding='UTF-8',newline='')
file_net.close() 

#Use English Wikipedia
wiki_wiki = wikipediaapi.Wikipedia('UniWork (merlin@example.com)','en')
i=0
for l in lines:
    page_py = wiki_wiki.page(l)
    links = get_links(page_py)
    print(i,l,len(lines))
    file_net = open(file_out, 'a', encoding='UTF-8',newline='')
    writer = csv.writer(file_net)
    for lk in links:
        lk = re.sub(' ',  '_', lk)  
        if (lk in lines):
            print("--->",l,lk)
            writer.writerow([l,lk])
    i = i + 1
file_net.close()    
