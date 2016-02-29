from __future__ import print_function
'''
Created on 19-May-2014

@author: pavang
'''

import pymongo
from pymongo import Connection

c = None
def create_db():
    global db
    c = Connection()
    db = c.qa
    
def create_collection():
    global ques
    ques = db.questions
    
def print_dict(dict_data, separator=':'):
     """
         print given dictionary and put separator between key and value
         while printing
     """
     for key, value in dict_data.items():
         print(str(key) + separator + '   ' + str(value))

def print_collections():
    pass

q1 = {
      "summary" : "What is the behaviour of Vijju",
      "description" : "He is a greatest Flipflop in this world",
      "tags" : ["human", "flip-flop", "Genda Swami"],
      "votes" : -5,
      "asked by" : "Sameer",
      "views" : 0,
      "favourites" : 2
      }

if __name__ == '__main__':
    create_db()
    create_collection()
#     ques.insert(q1)
    print_dict(ques.find_one())
#     print(ques.find_one())

    
    