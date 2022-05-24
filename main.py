from math import factorial as fact
n, k = [int(n) for n in input().split()]
#n = int(input())
def binomial(n, k):
    return fact(n) // fact(k) // fact(n-k)
print(binomial(n,k))