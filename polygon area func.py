def poly():
    import math
    print('To find the area of the polygon based on side, select: 1')
    print('To find the area of the polygon based on circumradius, select: 2')
    print('To find the area of the polygon based on apothem or inradius, select: 3')
    m=int(input('Please select an option to find the area: '))
    if m==1:
        s=float(input('Enter the length of the side: '))
        n=int(input('Enter the number of sides: '))
        f=((s**2)*n)/(4*math.tan(math.radians(180/n)))
        print('Area of the polygon is: ',round(f,2))


    if m==2:
        r=float(input('Enter the circumradius of the side: '))
        n=int(input('Enter the number of sides: '))
        f= ((r**2)*n*(math.sin(math.radians(360/n))))/2
        print('Area of the polygon is: ',round(f,2))

    if m==3:
        a=float(input('Enter the inradius or apothem of the side: '))
        n=int(input('Enter the number of sides: '))
        f=(a**2)*n*(math.tan(math.radians(180/n)))
        print('Area of the polygon is: ',round(f,2))
