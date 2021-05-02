n=int(input("Enter n'th number: "))

def isprime(n):
    c=0
    for i in range(1,n+1):  #numbers to check if it is prime or not
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
for i in range(1,n+1):
    if(isprime(i)):
        print(i)

# both are with same logic

for x in range(1,n+1):
    c=0
    for i in range(1,x+1): 
        if(x%i==0):
            c=c+1
    if(c==2):
        print(x)
