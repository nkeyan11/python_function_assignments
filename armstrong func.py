def armstrong(n):
    
    p=len(n)
    q=int(n)
    val=0
    for i in range(0,p):
        a=pow(int(n[i]),p)
        val=val+a

    if val==q:
        print('The given number is armstrong number')
    else:
        print('The given number is not armstrong number')
