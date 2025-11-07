def loop_fibbonacci(n):
    step_count = 0
    first = 0
    second = 1
    print(first, end=" ")
    print (second, end=" ")
    while (n-2>0):
        third= first+second
        first,second = second,third
        print(third,end=" ")
        n-=1
        step_count+=1
    print()
    print(step_count)

n=int(input("Enter the number ofterms you want in Fibonacci series: "))

loop_fibbonacci(n)


