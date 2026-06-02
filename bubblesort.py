arr1 = [10,20,50,40] 
 
def bubble(arr1): 
    n = len(arr1) 
    for i in range(n): 
        swapped = False 
        for j in range(0,-i-1): 
            if arr1[j]>arr1[j+1]: 
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j] 
                swapped = True 
            if not swapped: 
                break 
arr1 = [10,20,30,40] 
bubble(arr1) 
print("sort arry-", arr1)