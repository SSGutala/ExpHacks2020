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
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import cosine_similarity

#stem words = like, liked, likely  


def get_feature_matrix(texts, vocabulary):
    num_rows = len(texts) #in this situation there would be 4 since 4 scenarios
    #print("num rows is " +  str(num_rows))
    matrix = np.zeros([num_rows, len(vocabulary)]) #creates a matrix with all zeroes of 4 X num of words in vocab
    #print(matrix)
    i = 0 
    for text in texts:
        for word in text:
            # if current word in vocabulary
            # assign cell with index (review number, id of the word in the dict) with 1
            if word in vocabulary:
                matrix[i,vocabulary[word]] = 1 
        i = i + 1
    return matrix 


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
    ones_list =[]
    for i in train_data:
        if i != []:
            ones_list.append(i.pop(0))
    #print(ones_list)
    #print(big_vocabulary) 
    train_matrix = get_feature_matrix(train_data, big_vocabulary) 
    #print(train_matrix) 
    testconvo = open("user_image.txt", "r+")
    test_data = testconvo.read() 
    
    test_d = []
    test_d.append(test_data) 
    test_matrix = get_feature_matrix(test_d, big_vocabulary)
    #print(test_matrix[0]) 
    cos = np.dot(train_matrix[0], test_matrix[0]) / (np.sqrt(np.dot(train_matrix[0],train_matrix[0])) * np.sqrt(np.dot(test_matrix[0],test_matrix[0])))
    #print("distance is " + cosine_similarity(train_matrix[0], test_matrix[0]))
    #print(big_vocabulary)
    cos1 = np.dot(train_matrix[1], test_matrix[0]) / (np.sqrt(np.dot(train_matrix[1],train_matrix[1])) * np.sqrt(np.dot(test_matrix[0],test_matrix[0])))
    cosines = []
    for i in range(len(train_matrix) - 1):
            cos = np.dot(train_matrix[i], test_matrix[0]) / (np.sqrt(np.dot(train_matrix[i],train_matrix[i])) * np.sqrt(np.dot(test_matrix[0],test_matrix[0])))
            cosines.append(cos)
    #print(cosines) 
    max_index = cosines.index(max(cosines))
    label = ones_list[max_index]
    #print(label)
    if(label == "+1") :
        print("FAKE ADVERTISEMENT POSSIBILITY")
    elif (label == "-1") :
        print("REAL ADVERTISEMENT")
    