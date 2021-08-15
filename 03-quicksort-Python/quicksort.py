"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(arr, lo, hi):
	pivot = arr[lo]
	i = lo
	for j in range(lo+1, hi+1):
		if arr[j] < pivot:
			i+=1
			(arr[i], arr[j]) = (arr[j], arr[i])
	(arr[i], arr[lo]) = (arr[lo], arr[i])
	return i		

def sort(array, lo, hi):
	if lo < hi:
		p = partition(array, lo, hi)
		sort(array, lo, p-1)
		sort(array, p+1, hi)
	return array

def quicksort(array):
	return sort(array, 0, len(array)-1)