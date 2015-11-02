ns_count = {'10.71.71.187:3000': ['test', 'bar'], '10.71.71.49:3000': ['test', 'bar']}


def unanimous(ns_count):
    it = iter(ns_count)
    first = it.next()
    return all(i == first for i in it)


if __name__ ==  '__main__':
    print unanimous(ns_count.values())

    
    
    
    
        
        