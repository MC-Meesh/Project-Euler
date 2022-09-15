fib4mil = [1, 2]
i=2
fib_num=0

while fib_num  <= 4*10**6:
    fib_num = fib4mil[i-1] + fib4mil[i-2]
    fib4mil.append(fib_num)
    i+=1

sum=0
for i in fib4mil:
    if (i%2==0):
        sum+=i

print(sum)