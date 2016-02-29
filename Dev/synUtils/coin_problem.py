def get_shortest_string(value):
    answer = ""
    

def get_value_for_string(string):
    value = 0
    for char in string:
        value += get_value(char)

    return value

def get_value(ch):
    if ch == 'A':
        return 1
    else:
        return (get_value( chr(ord(ch) - 1) ) * 2 + (ord(ch) - 64) )

 

if __name__ == '__main__':
   print get_value('D')
   print get_value_for_string('ABC')