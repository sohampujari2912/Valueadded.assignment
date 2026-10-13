#Lowest Common Multiple (LCM) of Two Numbers
 
def findLcm(n1, n2):
    if n1 ==0 or n2==0:
        return 0 

    a=abs(n1)
    b=abs(n2)

    x,y=a,b

    while y != 0:
        x, y= y,x%y

    return (a*b)//x   
    
