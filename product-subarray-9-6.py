#product of all subarrays from array

def subarray_product(arr, n):
	product = 1
	for i in range(0, n):
		for j in range(i, n):
			for k in range(i, j+1):
				product *= arr[j]

	print(product)

arr = [2, 5, 4]
#arr = [10, 3, 7]
subarray_product(arr, len(arr))

