
"""
Zotero API programming in order to edit tags
Written by **// Amirbahador Nasari //**
date: 27/6/2018
"""

#importing pyzetro API library and time package

import time
from pyzotero import zotero

# returning starting time

start=time.time()

# connecting to the server ("user/group ID","state","API key which can be found in zotero website")

#zot = zotero.Zotero('2034407', 'group', '5jwMQvNGcjk12KMn5HUsiJsp' )
zot = zotero.Zotero('4840414', 'user', '5jwMQvNGcjk12KMn5HUsiJsp' )

# checking key information

key=zot.key_info()

# retriving items

item=zot.everything(zot.items())

# obtaining excepted tags from the text file

with open('excepted.txt', 'r') as f:
    exceptedTags = [line.strip() for line in f]

# making new lists

tagslist=[]
tagslist_new=[]
tags=[]
inTagsButNotInNew=[]

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    
    # For item i in a range that is a length of l,
    
    for i in range(0, len(l), n):
        
        # Create an index range for l of n items:
        
        yield l[i:i+n]

# Define a modifier

def modifier(str):
    
    if "{\_}" in str:
        str=str.replace("{\_}"," ")
        
    if "\_" in str:
       str=str.replace("\_"," ")
        
    if "{\&}" in str:
       str=str.replace("{\&}","&")
       
    if str in exceptedTags:  
        return str
    
    else:
        return str.lower()

# this part is for handling the tags 

for i in range(len(item)):
    
    # clearing the lists

    tagslist.clear()
    tagslist_new.clear()
    tags.clear()
    
    tags=item[i]['data']['tags'] 
       
    for j in range(len(tags)):
        
        tagslist.append(tags[j]['tag'])
        tagslist_new.append(modifier(tags[j]['tag']))
        
    inTagsButNotInNew.extend(list(set(tagslist) - set(tagslist_new)))
    
    # adding modified tags
    zot.add_tags(item[i], *tagslist_new)
    
    
reduntlist=list(chunks(inTagsButNotInNew, 50))
    
# removing all redundant tags 

for i in range(len(reduntlist)):    
    zot.delete_tags(*reduntlist[i])
        
#returning ending time

end=time.time()

# displaying processing time in seconds

print( "processing time= " , end - start , "Seconds" )

# finishing notification 

print("Done Successfully!")             
       

    
    


  

