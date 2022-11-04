def swap_list(inputs):
    if len(inputs) % 2 == 0:
        middle = int(len(inputs) // 2) - 1 # middle left element
    else:
        middle = int(len(inputs) // 2)

    last = len(inputs) - 1
    
    inputs[last], inputs[middle] = inputs[middle], inputs[last]

    return inputs
