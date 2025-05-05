def selectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n-1):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
        print(f"Step {i+1}: {arr}")

n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    temp=int(input("Enter the number: "))
    arr.append(temp)

selectionSort(arr)
print("Sorted Array is: ",arr)
