def expOpCl(stack):
    for i in range(len(stack)):
        exp1 = stack.pop()
        exp2 = stack.pop()

        if(exp1 == '(' and exp2 == ')'):
            return 'closed'
        else:
            return 'retry'


def calculator(value):
    valInput = []
    opInput = []
    expInput = []
    flag = 0
    flag1 = 0
    for i in range(len(value)):  # Push values to stack
        if(value[i] != ' '): # Accounts for spacing
            if(value[i].isdigit()):
                valInput.append(int(value[i]))
                
            else:
                if(value[i] == '+' or value[i] == '-' or value[i] == '*' or value[i] == '/'): # operations
                    if(value[i] =='/'):
                        opInput.append(value[i])
                        if(value[i+1] == '/'):
                            opInput.append(value[i])
                            flag = 1
                    if(value[i] == '*'):
                        opInput.append(value[i])
                        if(value[i+1] == '*'):
                            opInput.append(value[i])
                            flag = 1
                else:
                    if(value[i] == '(' or value[i] == '{'):
                        opInput.append(value[i])


    op1 = valInput.pop()
    op2 = valInput.pop()

    for i in range(len(opInput)):
        if(len(expInput) == 0):
            if(opInput[i] == '+'):
                return op1 + op2
            elif(opInput[i] == '-'):
                return op1 - op2
            elif(opInput[i] == '*'):
                if(flag == 1): # exponent **
                    return pow(op1,op2)    
                else:
                    return op1 * op2
            elif(opInput[i] == '/'):
                if(flag == 1): # integer division
                    return int(op1 / op2)
                else:
                    return op1 / op2
        else:
            expOpCl(expInput)


           
print(calculator('(4*2'))

        