def emi(p,i,n):

    i=i/(12*100)
    e=(p*i*((1+i)**n))/((1+i)**(n-1))

    return round(e,2)
