__author__ = 'pavang'


movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#print(movies)

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)



#for m in movies:
#    if isinstance(m,list):
#        for shortMovie in m:
#            print(shortMovie)
#    else:
#        print(m)

