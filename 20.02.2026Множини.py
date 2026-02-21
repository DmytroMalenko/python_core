# Task 1
'''
new_nums = set()
nums = set(['1','2','3','4','5'])

nums = {'1','2','2','3','4','4','5'}
print(', '.join(nums))


# Task 2

new_nums = set()
nums1 = set(['1','2','3','4','5','6','7','8','9','10'])
nums2 = set(['11','12','13','14','15','16','17','18','19','20'])  

nums = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
print(', '.join(nums))

print(nums1 - nums2)

numbers = nums1.union(nums2)
numbers = nums1 | nums2
print(', '.join(nums))

'''
# Task 3

word1 = str(input("Write first word: "))
word2 = str(input("Write second word: "))

set1 = set(word1)
set2 = set(word2)

if set1 == set2:
    print("The words are anagrams.")
else:
    print("The words aren't anagrams.")