# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:40:11 2020

@author: sai.gutala
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:00:18 2020
@author: admin
"""

import PyPDF2
import numpy as np 
#import pdftotext
import nltk 
from nltk.tokenize import word_tokenize 
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#stem words = like, liked, likely  

def bag_of_words(texts) :
    vocabulary = {}
    for text in texts:
        #print(text)
        word = word_tokenize(text)
        #print(word)
        for a in word:           
            if a not in vocabulary:
                vocabulary[a] = len(vocabulary)
    return vocabulary 
        
    """
    Clean review (delete digits, special symbols, stopwords).
        
        :param text: text to clean
        :return: cleaned string
    """
    #filter special characters, digits,stopwords, and stem
    text = word_tokenize(text)
    clean = re.compile('<.*?:>')
    digits = re.compile('\d')
    commonwords = re.compile('Hey')
    stop_words = stopwords.words('english')
    text = re.sub(clean,'',text) 
    text = re.sub(digits,'',text) 
    
    text = re.sub(commonwords,'',text)
    
    #tokenize the texts
    text = word_tokenize(text.lower())
    #remove stopwords
    text = [word for word in text if word not in stop_words]
    return ''.join(text)
    #remove special charactes
    return ''.join(text)
    #remove digits
    text = [word for word in text if word not in digits]
    return ''.join(text)
    #remove Stem Words
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in text]
    print(stemmed[:100])
    #remove commondwords
    text = [word for word in text if word not in commonwords]
    return ''.join(text)
def get_data(filename):
    """
    Read data from file.
    :param filename: name of file to read
    :param return_labels: flag if the are labels in the file
    :return: list of lists
    """
    
    txtconvo = open("data.txt", "r+") #opens text conversation file and reads & writes it    
    store_convo = txtconvo.read() #stores conversation into thiss variable 
    
    store_convo = store_convo.lower()
    
    
    
    
# Ensures Random symbols don't pop up for apostrophes, accents, or ... and other such commmonly used Enlgish symbols
    store_convo = store_convo.replace("â€™","")
    store_convo = store_convo.replace("â€”","")
    store_convo = store_convo.replace("â€˜","")
    store_convo = store_convo.replace("Â©", "")
    store_convo = store_convo.replace("Â®","")
    store_convo = store_convo.replace("\n"," ")
    print(store_convo)
    
if __name__ == '__main__':
    train_data = get_data('data.txt')
    big_vocabulary = bag_of_words(train_data)
    print(big_vocabulary)
