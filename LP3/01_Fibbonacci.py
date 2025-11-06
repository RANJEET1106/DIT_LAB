def recurs_fibbonacci(n):
    if n<=1:
        return n
    return recurs_fibbonacci(n-1)+recurs_fibbonacci(n-2)

def loop_fibbonacci(n):
    first = 0
    second = 1
    print(first, end=" ")
    print (second, end=" ")
    while (n-2>0):
        third= first+second
        first,second = second,third
        print(third,end=" ")
        n-=1
    print()

n=10
for i in range (n):
    print(recurs_fibbonacci(i), end = " ")
print()

loop_fibbonacci(n)


