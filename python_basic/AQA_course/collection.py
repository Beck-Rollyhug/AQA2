# 1
nums1 = [1, 2, 3].append(4)
print(f"1: {nums1}")

# 2
nums2 = ['A', 'B', 'C'].remove('B')
print(f"2: {nums2}")

# 3
nums3 = ['A', 'B', 'C']
print(f"3: {nums3[1]}")

# 4
nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"4: {nums4[3:7]}")

# 5
nums5 = ['A', 'B', 'C'][1] = 'D'
print(f"5: {nums5}")

# 6
nums6 = ['A', 'B', 'C']
print(f"6: {len(nums6)}")

# 7
nums7 = {'a': 1, 'b': 2}['c'] = 3
print(f"7: {nums7}")

# 8
nums8 = {'a': 1, 'b': 2}['b'] = 3
print(f"8: {nums8}")

# 9
nums9 = {'a': 1, 'b': 2}
del nums9['b']
print(f"9: {nums9}")

# 10
nums10 = {'a': 1, 'b': 2}['b']
print(f"10: {nums10}")

# 11
nums11 = {'a': 1, 'b': 2}
print(f"11: {'b' in nums11}")

# 12
nums12 = {'a': 1, 'b': 2, 'c': {'c1': 0, 'c2': 10}}
nums12['c']['c1'] = 1
print(f"12: {nums12}")

# 13
nums13 = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
nums13['c'][0] = 0
print(f"13: {nums13}")

# 14
nums14 = [{'a': 1, 'b': 2}]
nums14[0]['a'] = 0
print(f"14: {nums14}")

# 15
nums15 = (1, 2, 3, 4)
print(f"15: {1 in nums15}, {len(nums15)}")
