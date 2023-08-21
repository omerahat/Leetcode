def isValidSudoku(board):
    
    def createSet(line):
        s = set()
        for i in line:
            if i != ".":
                s.add(i)
        return s
    
    def createList(line):
        l = []
        for i in line:
            if i != ".":
                l.append(i)
        return l

    # check rows
    for row in board:
        if len(createSet(row)) != len(createList(row)):
            print(row)
            print(set(row))
            return False
    # check columns
    for i in range(len(board)): 
        column = []
        for row in board:
            column.append(row[i])
        if len(createSet(column)) != len(createList(column)):
            return False
    
    # check 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = []
            for row in board[i:i+3]:
                square.extend(row[j:j+3])
            if len(createSet(square)) != len(createList(square)):
                return False

    return True
