# encoding=utf-8
import time

# return one match result
def binary_search(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = first + (last - first) // 2
        print('[INFO] Current Position:{}'.format(mid))
        if nums[mid] > target:
            last = mid - 1
        elif nums[mid] < target:
            first = mid + 1
        else:
            return mid
    return -1

# [UnComplete] If need return all searched result
# result_list = set()
# def binary_search(nums, target):
# 	first = 0
# 	last = len(nums) - 1 

# 	while first <= last:
# 		mid = first + (last - first) // 2
# 		print('[INFO] Current Position:{}'.format(mid))
# 		if nums[mid] < target:
# 			first = mid + 1
# 		elif nums[mid] > target:
# 			last = mid - 1
# 		else:
# 			result_list.add(mid)
# 			print('Target index:',mid)
# 			if first != last:
# 				left_nums = nums[:mid-1]
# 				print('left_nums',left_nums)
# 				return binary_search(left_nums, target)
# 				right_nums = nums[mid+1:]
# 				print('right_nums',right_nums)
# 				return binary_search(right_nums, target)
# 		time.sleep(3)

# 	if len(result_list) == 0:
# 		result_list.add(-1)
# 	return result_list

def test():
	# nums = [1,2,2,4,5,5]; target = 2
	nums = [1,2,2,4,5,5]; target = 6
	target_position = binary_search(nums, target)
	print('[INFO] The Target Position is:',(target_position))

if __name__ == '__main__':
	test()
	