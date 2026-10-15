import random
n=int(input("Enter length of password: "))

def pgen(n):

    password = " "
    charset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXVZ123456789"
    for i in range(1,n+1):
        password = password + random.choice(charset)
        print(password)


pgen(n)
