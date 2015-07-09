'''
Created on Jul 19, 2014

@author: pavang
'''

class operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)
        
class properties(object): # Need object in 2.X for setters
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, None)
    
class propertiesNotation(object):
    @property
    def age(self):
        return 40
    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':
#     x = operators()
#     print(x.age)
#     print(x.job)

#     xp = properties()
#     xp.age = 45
#     print(xp.age)
#     print(properties.__dict__)
    
    pn = propertiesNotation()
    pn.age = 60
    print(pn.age)
       
    
    
    pass