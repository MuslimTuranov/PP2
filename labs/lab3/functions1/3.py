def solve(x, y):
    a = x * 2
    b = y - a
    if b == 0:
        print("chickens: ", x)
        print("rabbits: ", b)
    else:
        y = b / 2
        x = x - y
        print("chickens: ", x)
        print("rabbits: ", y)
        
solve(35, 94)
        
    
    

