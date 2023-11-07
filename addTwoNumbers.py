# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return numToReversedArr(arrToNum(l1) + arrToNum(l2))
def arrToNum(arr):
    sum = 0
    i = 1
    step = 0
    while(step < len(arr)):
        sum += arr[step] * i
        i *= 10
        step+=1
    return sum

def numToReversedArr(num):
    step = 0
    helper = 10
    digits = []
    while(step < len(str(num))):
        fraction, remainder = divmod(num, helper)
        digit = remainder // (helper / 10)
        digits.append(math.floor(digit) )
        step+=1
        helper *= 10
    return digits


sol = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(sol.addTwoNumbers(l1, l2))
