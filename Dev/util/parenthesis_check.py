'''
Created on 01-May-2014

@author: pavang
'''
def parenthesis(input_str):
    lst = []
    opposite_char = { ')':'(', '}':'{', ']':'[' }
    for ch in input_str:
        if ch in ['(', '{', '[']:
            lst.append(ch)
        elif ch in [')','}',']']:
            if not lst or lst[-1] != opposite_char[ch]:
                return False
            else:
                lst.pop()   
        else:
            continue
    return True  
         
if __name__ == '__main__':
    input_str = "()"
    print(parenthesis(input_str))
    