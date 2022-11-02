def sort_dictionary(values):
    values = sorted(values.items(), key=lambda item: item[1][1])
    print("{ ", end="")
    for index, item in enumerate(values):
        if(index == len(values) - 1):
            print('(\'{Name}\',{Phone})'.format(Name=item[0],Phone=item[1][0]), end=" ")
        else:
           print('(\'{Name}\',{Phone})'.format(Name=item[0],Phone=item[1][0]), end=", ") 
    print("}")    
test =  {'Tom': (5464512, 24), 'Sara':(5446987, 32), 'Mary' : (1557896, 20)}

sort_dictionary(test)


