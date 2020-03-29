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
        for word in text:           
            if word not in vocabulary:
                vocabulary[word] = len(vocabulary)
    return vocabulary 
    


def get_data(filename):
    """
    Read data from file.
    :param filename: name of file to read
    :param return_labels: flag if the are labels in the file
    :return: list of lists
    """

    txtconvo = open(filename, "r+") #opens text conversation file and reads & writes it
    store_convo = txtconvo.read() #stores conversation into this variable 
    chats = store_convo.split("--------------------")
    new_list = []
    for i in chats:
        texts_words = word_tokenize(i)
        new_list.append(texts_words)
# Ensures Random symbols don't pop up for apostrophes, accents, or ... and other such commmonly used Enlgish symbols
  
    #print(store_convo) 
    return new_list
    
if __name__ == '__main__':
    train_data = get_data('data.txt')
    big_vocabulary = bag_of_words(train_data)
    print(big_vocabulary) 
    #print(big_vocabulary)