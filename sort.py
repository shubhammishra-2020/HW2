def sort_dictionary(values):
    values = sorted(values.items(), key=lambda item: item[1][1])
    res = []
    for item in values:
        res.append((item[0], item[1][0]))
    return res
        
        


