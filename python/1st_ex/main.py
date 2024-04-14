x_start = -3
x_end = 7
dx = int(input("Input step: "))

if dx <= 0:
    raise Exception("Invalid input")

for x in range(x_start, x_end + 1, dx):
    print(x, end=' ')
    if x <= -1: 
        print(-x - 1, end='\n')
    elif x <= 1:
        print(0, end='\n')
    elif x <= 5:
        print((4 - (x - 3) ** 2) ** 0.5, end='\n')
    else:
        print(-0.5 * x  + 2.5, end='\n')
