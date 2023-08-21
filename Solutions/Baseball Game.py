def calPoints(operations):
    
    stack = []
     
    for i in operations:
        if i not in ["C","D","+"]:
            stack.append(int(i))
        elif i == "C":
            stack.pop()
        elif i == "D":
            stack.append(int(stack[-1])*2)
        elif i == "+":
            stack.append(int(stack[-1])+int(stack[-2]))

    return sum(stack)
