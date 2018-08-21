# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 01:41:02 2018

@author: shurastogi
"""

def filter_long_words(list_ex,n):
    return [x for x in list_ex if(len(x)>n)]
    