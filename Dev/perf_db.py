'''
Created on Jan 14, 2015

@author: pavang
'''
from mongoengine import *

# Create your models here.
connect('perf')

class DailyOpenPerformance(Document):
    display_name = StringField()
    reputation = IntField()


if __name__ == '__main__':
    dop = DailyOpenPerformance()
    print("DB Created")
    
    pass