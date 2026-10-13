 #Count of Prime Numbers till N

def countPrimes(n):
    count=0

    for num in range(2,n+1):
        is_prime=True

        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break

        if is_prime:
            count+=1
    return count                
    