def sort_dictionary(values):
    values = sorted(values.items(), key=lambda item: item[1][1])
    

        
test =  {'Tom': (5464512, 24), 'Sara':(5446987, 32), 'Mary' : (1557896, 20)}

sort_dictionary(test)


