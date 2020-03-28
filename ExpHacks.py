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

#stem words = like, liked, likely  

def bag_of_words(texts) :
    vocabulary = {}
    for text in texts:
        for word in text:
            if word not in vocabulary:
                vocabulary[word] = len(vocabulary)
    return vocabulary 


def get_feature_matrix(texts, vocabulary):
    num_rows = len(texts) #in this situation there would be 4 since 4 scenarios
    matrix = np.zeros([num_rows, len(vocabulary)]) #creates a matrix with all zeroes of 4 X num of words in vocab
    for i, text in texts:
        for word in text:
            # if current word in vocabulary
            # assign cell with index (review number, id of the word in the dict) with 1
            if word in vocabulary:
                matrix[i,vocabulary[word]] = 1 
    return matrix 


def get_data(filename, return_labels=False):
    """
    Read data from file.
    :param filename: name of file to read
    :param return_labels: flag if the are labels in the file
    :return: list of lists
    """

txtconvo = open("sample_convo1.txt", "r+") #opens text conversation file and reads & writes it
store_convo = txtconvo.read() #stores conversation into thiss variable 

# Ensures Random symbols don't pop up for apostrophes, accents, or ... and other such commmonly used Enlgish symbols
store_convo = store_convo.replace("â€™","") 
store_convo = store_convo.replace("â€“","")
store_convo = store_convo.replace("â€¦","")
chats = store_convo.split('--------------------------------------------------------------------------------------------------------------------')

new_list = [] 

for i in chats:
    
    texts = getwordsfunc(i)
    
    new_list.append(text)    
    #save in variable - add (append) variable to list 

print(new_list)
    

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
    
if __name__ == '__main__':
    file1 = open("messages.txt", "r+")
    message = file1.read()
    message = message.replace("â€™","")
    message = message.replace("â€“","")
    chats = message.split('\n')
    for i in chats:
        print(i) 
        print(word_tokenize(i))
        
    

    








