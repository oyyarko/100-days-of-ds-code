#binary search

#create recursive function

def binary_search(arr, l, r, x):
	if r>=l:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, l, mid-1, x)
		else:
			return binary_search(arr, mid+1, r, x) 
	else:
		return -1

arr = [2, 5, 9, 15, 23, 38, 63]
x = 25

result = binary_search(arr, 0, len(arr), x)
if result != -1:
	print('{} Element found at: {}'.format(x, result))
else:
	print('Not found from : {}'.format(arr))
