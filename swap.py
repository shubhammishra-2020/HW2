def swap_list(inputs):
    if len(inputs) % 2 == 0:
        middle1stInd = int(len(inputs) / 2)
        middle2ndInd = int(len(inputs) / 2) - 1
        middle1st = inputs[middle1stInd]
        middle2nd = inputs[middle2ndInd]
        middle = (middle1st + middle2nd) / 2 
    else:
        middle = int(len(inputs) / 2)
        

    last = len(inputs) - 1
    inputs[last], inputs[middle] = inputs[middle], inputs[last]
    

