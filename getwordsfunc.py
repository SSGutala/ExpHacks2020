# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:38:09 2020

@author: sai.gutala
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def getwordsfunc(text):
    
    """
    Clean review (delete digits, special symbols, stopwords).
        
        :param text: text to clean
        :return: cleaned string
    """
    #filter special characters, digits,stopwords, and stem
    
    clean = re.compile('<.*?>')
    digits = re.compile('\d')
    commonwords = re.search('Hey')
    stop_words = stopwords.words('english')
    text = re.sub(clean,'',text) 
    text = re.sub(digits,'',text) 
    
    text = re.sub(commonwords,'',text)
    
    #tokenize the texts
    text = word_tokenize(text.lower())
    #remove stopwords
    text = [word for word in text if word not in stop_words]
    
    return ''.join(text)

    #remove Stem Words
    
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in text]
    
    print(stemmed[:100])
    
    #remove commondwords
    
    text = [word for word in text if word not in commonwords]
    return ''.join(text)