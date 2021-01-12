def binary_search(input, target):
    length = len(input)
    if length == 0:
        return -1
    mid_index = length // 2
    mid_value = input[mid_index]
    front = input[:mid_index]
    back = input[mid_index + 1:]
    if mid_value == target:
        return mid_index
    elif length == 1 and mid_value != target:
        return -1
    elif mid_value > target:
        return binary_search(front, target)
    elif mid_value < target:
        return binary_search(back, target)

print(binary_search([1,2,3,4], 1)) # => 0
print(binary_search([1,2,3,4], 2)) # => 1
print(binary_search([1,2,3,4], 3)) # => 2
print(binary_search([1,2,3,4], 4)) # => 3
print(binary_search([1,2,3,4], 5)) # => -1
print(binary_search([1,2,3,4,5], 1)) # => 0
print(binary_search([1,2,3,4,5], 2)) # => 1
print(binary_search([1,2,3,4,5], 3)) # => 2
print(binary_search([1,2,3,4,5], 4)) # => 3
print(binary_search([1,2,3,4,5], 5)) # => 4
print(binary_search([1,2,3,4,5], 6)) # => -1