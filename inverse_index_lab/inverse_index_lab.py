from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    i = 0
    d = {}
    for s in strlist:
        words = s.split()
        for w in words:
            if  w in d:
                d[w].add(i)
            else:
                d[w] = {i}
        i += 1
    return d
    
    

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    s = set()
    for word in query:
        for doc in inverseIndex[word]:
            s.add(doc)
    return s
        

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    s=set()
    i = 0
    for word in query:
       t = set()
       for doc in inverseIndex[word]:
           t.add(doc)
           if i == 0: s.add(doc) 
       i+=1
       s.intersection_update(t) 
          
    return s

def main():
    strList = []
    f = open("stories_big.txt")
    for line in f:
        strList.append(line)     
   
    d = makeInverseIndex(strList)
#    for k in sorted (d):
#        print (k, d[k])
    s = orSearch(d, ["you", "train"])
    print(s)
    s = andSearch(d, ["you", "train"])
    print(s)
        
main()
    
    
        
