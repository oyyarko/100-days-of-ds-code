## Linear Search
'''
Input : arr[] = {10, 20, 80, 30, 60, 50, 
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

'''
def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i
    return -1
  
# Driver Code 
arr = [20, 30, 40, 10, 50, 60, 70, 80, 90, 100]
#x = 10
x = int(input('Enter Element: '))
n = len(arr)
result = search(arr, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result)
