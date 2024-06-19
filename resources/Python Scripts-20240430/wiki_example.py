# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 23:48:36 2022

@author: 451966
"""

import wikipediaapi


def get_links(page):
    links = page.links
    filtered_links = []
    for lk in sorted(links.keys()):
        if (lk.find("Category")==-1 and lk.find("Template")==-1 and lk.find("Wikipedia")==-1):
            filtered_links.append(lk)
    return filtered_links


def get_backlinks(page):
    links = page.backlinks
    filtered_links = []
    for lk in sorted(links.keys()):
        if (lk.find("Category")==-1 and lk.find("Template")==-1 and lk.find("Wikipedia")==-1):
            filtered_links.append(lk)
    return filtered_links    


#Use English Wikipedia
#how to use Wikipedia-api
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Regensburg')

#check if the page exists
print("Page - Exists: %s" % page_py.exists())

#print the title    
print(page_py.title)

#get the links    
links = get_links(page_py)
print("Number of links",len(links))

backlinks = get_backlinks(page_py)
print("Number of backlinks",len(backlinks))
