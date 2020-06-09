#finding subsets from array
'''
Input: arr[] = {1, 2, 3, 4}, K = 5
Output: {2, 3}, {1, 4} '''

def find_subsets(arr, n):

	x = pow(2, len(arr))
	counter, j = 0, 0

	for counter in range(0, x):
		for j in range(0, n):
			if((counter & (1 << j)) > 0):
				print(arr[j], end = "")
		print("")

arr = ['2', '3', '4']
find_subsets(arr, len(arr))
