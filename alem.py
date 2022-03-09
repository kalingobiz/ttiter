# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 01:24:12 2020

@author: kalingolive
"""
from nltk.tokenize import word_tokenize
import urllib.request  
import codecs
import os
from bs4 import BeautifulSoup


def prepare(addr):
    
    f = codecs.open("asiteyayet0b08.html","r","utf-8")
    items = []
    titles = []
    detail_loc = []
    samples = f.read().split('<div class="categories-view-content view-content-wrap layout-list">')
    sample = samples[1].split('<div class="item">')
    bread = samples[0].split('<h2 id="system-breadcrumb" class="visually-hidden">Breadcrumb</h2>')
    group = bread[1].split("መነሻ ገጽ</a>\n<span>&nbsp;/&nbsp;</span>\n</li>\n<li>\n</li>\n<li>")[1].split('\n</li>')[0].split()
    group = ''.join(group)
    for i in range(1,11):
        loc = sample[i].split('about="/')[1].split('typeof=')[0].split('"')[0]+".html"
        detail_loc.append(loc)
        file = codecs.open(loc,"r","utf-8")
        detail =  file.read().split('<div property="schema:text" class="field field--name-body field--type-text-with-summary field--label-hidden field__item">')[1].split('ከአዘጋጁ')[0].split("<strong>")[0]
        itemi = sample[i].split('<span property="schema:name">')
        titles.append(itemi[1].split('</span>')[0])
    #    items.append(itemi[1].split('<div property="schema:text" class="field field--name-body field--type-text-with-summary field--label-hidden field__item">')[1].
    #                 split('</div>')[0].split('</div>\n</div>\n')[0])
        detail = detail.replace("<span>","").replace("</span>","").replace("<p>","").replace("</p>","").replace("\n","").replace("\xa0","").replace("<li>","").replace("</li>","").replace("<ol>","").replace("</ol>","").replace("<ul>","").replace("</ul>","")
        items.append(detail)
    
    
    print('=============================================================================================')    
    print('\t\t\t',group,'\t\t\t')
    print('=============================================================================================')    
    
    for i in range(len(items)):
        print(titles[i],"\n")
        print(items[i],"\n")
        print("---------------------------------------------------------------------------------------------")
        print("Detail of the article in: ", detail_loc[i])
        print('=============================================================================================')

dirs = os.listdir()
for fils in dirs:
    if "alem" in fils:
        print(fils)
        prepare(fils)
#dirs.pop(3)
#print(dirs)    
#content = ''.join(sample[1]).split('<nav')
#con = content[0].split('<item')
#
#html = urllib.request.urlopen("alem.html")
#file = open("alem.html","r+")
#sample = file.read().split('categories-view-content view-content-wrap layout-list')
#content = ''.join(sample[1]).split('<nav')
#tok = word_tokenize(sample)
#print(tok)
#
##<div class="categories-view-content view-content-wrap layout-list">
