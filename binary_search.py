import time

def bs1(array, value):

	front = 0
	end = len(array) - 1

	while front <= end:
		mid = int((front + end)/2.0)
		if array[mid] < value:
			front = mid + 1
		elif array[mid] > value:
			end = mid - 1
		else:
			return mid

	# not find position of the value
	return -1

def bs2(array, value, front, end):
	if front > end:
		return -1
	else:
		mid = int((front + end)/2.0)
		if array[mid] > value:
				end = mid - 1
				return bs2(array, value, front, end)
		elif array[mid] < value:
			front = mid + 1
			return bs2(array, value, front, end)
		else:
			return mid


def main():

	# init array and value
	array1 = [1,3,4,6,8,12,13,55,100]
	array2 = [2,3]
	value1 = 4
	value2 = 2

	start = time.time()
	# test
	assert bs1(array1, value1) == 2
	assert bs1(array1, value2) == -1
	assert bs1(array2, value1) == -1
	assert bs1(array2, value2) == 0
	end = time.time()
	print(end - start)
	
	# init front and end
	front = 0
	end1 = len(array1)-1
	end2 = len(array2)-1

	start = time.time()
	assert bs2(array1, value1, front, end1) == 2
	assert bs2(array1, value2, front, end1) == -1
	assert bs2(array2, value1, front, end2) == -1
	assert bs2(array2, value2, front, end2) == 0
	end = time.time()
	print(end - start)

if __name__ == "__main__":
	main()
