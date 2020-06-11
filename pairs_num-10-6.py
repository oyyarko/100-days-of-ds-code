from bisect import bisect_left as lower_bound

def find_num_of_pairs(a, n):
	a = sorted(a)
	ans = 0
	for i in range(n):
		if a[i] <= 0:
			continue
		j = lower_bound(a, -a[i]+1)
		ans += i-j
	return ans

if __name__ == '__main__':
	a = [5, -2, 3, -4, 6, 8, -7]
	ans = find_num_of_pairs(a, len(a))
	print(ans)
