def sc():
    import math
    print('Please select the operations from below for scientific calculator')
    print('1. Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Factorial, 6.Square, 7.Squareroot, 8.sin, 9.cos, 10.tan, 11.ln, 12.Radians, 13.log, 14.exponent, 0 to exit ')
    n=1
    while n!=0:
        
        n=int(input('Enter your choice'))
        if n==0:break
        if n==1:
            a=float(input('Enter the 1st number'))
            b=float(input('Enter the 2nd number'))
            print('The sum is', a+b)

        if n==2:
            a=float(input('Enter the 1st number'))
            b=float(input('Enter the 2nd number'))
            print('The difference is', a-b)

        if n==3:
            a=float(input('Enter the 1st number'))
            b=float(input('Enter the 2nd number'))
            print('The product is', a*b)

        if n==4:
            a=float(input('Enter the 1st number'))
            b=float(input('Enter the 2nd number'))
            print('The division is', a/b)

        if n==5:
            a=float(input('Enter the number'))
            print('The output is', math.factorial(a))

        if n==6:
            a=float(input('Enter the number'))
            
            print('The output is', a**2)

        if n==7:
            a=float(input('Enter the number'))
            
            print('The output is', math.sqrt(a))

        if n==8:
            a=float(input('Enter the number'))
            
            print('The output is', math.sin(math.radians(a)))

        if n==9:
            a=float(input('Enter the number'))
            
            print('The output is', math.cos(math.radians(a)))

        if n==10:
            a=float(input('Enter the number'))
            
            print('The output is', math.tan(math.radians(a)))

        if n==11:
            a=float(input('Enter the number'))
            
            print('The output is', math.log(a))
        if n==12:
            a=float(input('Enter the number'))
            
            print('The output is', math.radians(a))

        if n==13:
            a=float(input('Enter the number'))
            
            print('The output is', math.log10(a))

        if n==14:
            a=float(input('Enter the number'))
            b=float(input('Enter the exponent number'))
            print('The output is', math.pow(a,b))
        notn=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        if n not in notn:
            print('Invalid input')
            continue

sc()

