"""
python 实现归并排序
"""
from collections import deque

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged, left, right = [], deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft()) # 队列的左侧弹出时间复杂度同样是O(1)
        merged.extend(right if right else left)
        return merged

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

print(merge_sort([1,3,4,9,6,5]))
