from math import factorial as fact
k = int(input())
n = int(input())
def binomial(n,k):
    return fact(n) // fact(k) // fact(n-k)
print(binomial(k,n))