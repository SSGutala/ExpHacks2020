# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:00:18 2020

@author: admin

"""

import PyPDF2
#import pdftotext
 


mypdfFile = PyPDF2.PdfFileReader('chats.pdf') 
with open('output.txt', 'w') as pdf_output:
   for page in range(mypdfFile.getNumPages()):
       data = mypdfFile.getPage(page).extractText()
       pdf_output.write(data)
file1 = open("output.txt", "r+")
message1 = file1.read()
#print(message1) 
# Load your PDF
#with open("chats.pdf", "rb") as f:
#    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
#with open('output.txt', 'w') as f:
#    f.write("\n\n".join(pdf))
    



#chats = page.extractText()


#chats = chats.replace("’","")
#print(chats) 
#ls = chats.split('\n')
file1 = open("messages.txt", "r+")
message = file1.read()
message = message.replace("â€™","")
message = message.replace("â€“","")
chats = message.split('\n')
for i in chats:
    print(i) 
    
        
    








