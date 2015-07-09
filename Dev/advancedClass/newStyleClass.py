'''
Created on Jul 12, 2014

@author: pavang
'''

class C:
    data = 'spam'
    def __getattr__(self, name):                # Classic in 2.X: catches built-ins
        print(name)
        return getattr(self.data, name)

if __name__ == '__main__':
    x = C()
    print(x[0])
    
    