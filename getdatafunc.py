# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:40:11 2020

@author: sai.gutala
"""

def get_data(filename, return_labels=False):
    """
    Read data from file.

    :param filename: name of file to read
    :param return_labels: flag if the are labels in the file
    :return: list of lists
    """
    # create empty list
    
    import PyPDF2
#import pdftotext
 

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
    
  
 