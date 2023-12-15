def partition(arr,start,end):
    pivot=arr[start]
    lower_bound=start+1
    upper_bound=end

    while True:
        while lower_bound<=upper_bound and arr[lower_bound]<=pivot:
                lower_bound+=1
        while lower_bound<=upper_bound and arr[upper_bound]>=pivot:
                upper_bound-=1
        if lower_bound<upper_bound:
            arr[lower_bound],arr[upper_bound]=arr[upper_bound],arr[lower_bound]
        else:
            break
    
    arr[start],arr[upper_bound]=arr[upper_bound],arr[start]
    return upper_bound

def quickSort(arr,start,end):
    if(start<=end):
        ub=partition(arr,start,end)
        quickSort(arr,start,ub-1)
        quickSort(arr,ub+1,end)

arr=[54,26,93,17,77,31,44,55,20]
quickSort(arr,0,len(arr)-1)
print(arr)
