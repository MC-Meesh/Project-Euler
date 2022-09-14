# find the sum of numbers from 1-1000 thatare  also divisible  by 3 or 5
from audioop import mul


multiples = []
for i in range(0,1000):
    if ((i%5==0)|(i%3==0)):
        multiples.append(i)

sum = sum(multiples)
print(sum)
