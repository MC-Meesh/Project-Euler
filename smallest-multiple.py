#lowest number evenly divisible by 1-20
import pandas as pd
import numpy as np

#prime factorization of num
def primeFactors(num):
    primes = []
    prime = 2
    while(num>1):
        if(num%prime==0):
            primes.append(prime)
            num /= prime
        else:
            prime+=1
    
    return primes

#setup prime arrays
prime_max = [1, 2, 3, 5, 7,11, 13, 17, 19]
prime = [0]*20
unique_primes = [0]*20
total=1

for i in range(1,21):
    #find primes for each number 1-20
    prime[i-1] = primeFactors(i)
    unique_primes[i-1] = np.unique(np.array(prime[i-1]))

    #if there are more prime factors, append another (only increment by 1 given the way primes work)
    for j in unique_primes[i-1]:
        if (prime[i-1].count(j) > prime_max.count(j)):
            prime_max.append(j)

#multiply whole list 
for element in prime_max:
    total *= element

print(total)