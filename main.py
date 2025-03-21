# class Solution:
#     def twoSum(self, nums, target: int) :
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]

#         return []

# salom=Solution()
# d=salom.twoSum([2,7,11,15],9)
# print(d)

# Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int):
#         if x>=0:
#             return x==int(str(x)[::-1])
#         return False


# salom = Solution()
# d=salom.isPalindrome(120)
# print(d)

# Roman to Integer

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         value = 0
#         last_digit_value = 0
        
#         for roman_digit in num[::-1]:            
#             digit_value = value_map[roman_digit]

#             if digit_value >= last_digit_value:       
#                 value += digit_value         
#                 last_digit_value = digit_value
#             else:                                     
#                 value -= digit_value

#         return value
        
