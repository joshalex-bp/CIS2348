#Joshua Guajardo     PSID:1811892


I1 = int(input())
I2 = int(input())
I3 = int(input())
I4 = int(input())
I5 = int(input())
I6 = int(input())

solution = False
for x in range(-10, 11):
    for y in range(-10, 11):
         if I1 * x + I2 * y == I3 and I4 * x + I5 * y == I6:
            print(x, y)
            solution = True

if solution == False:
    print('No solution')



