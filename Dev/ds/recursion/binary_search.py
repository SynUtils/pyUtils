'''
Created on Aug 12, 2014

@author: pavang
'''

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = int((low + high ) / 2)
        if data[mid] == target:
            return True
        elif target > data[mid]:
            return (binary_search(data, target, mid + 1, high)) 
        else:
            return(binary_search(data, target, low, mid-1))

if __name__ == '__main__':
    data = [1,3,5,7,9]
    print(binary_search(data, 9, 0, 4))
    
    
    pass