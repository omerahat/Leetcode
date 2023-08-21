def dailyTemperatures(temperatures):

    result = [0] * len(temperatures)
    stack = [] # [temp & index]

    for index,temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][0]:
            stackTemp , stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append((temperature,index))

    return result
