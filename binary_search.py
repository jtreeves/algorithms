def binary_search(input, target):
    length = len(input)
    midpoint = length // 2
    front = input[:midpoint]
    back = input[midpoint:]
    if length == 1:
        if input[midpoint] == target:
            return True
        else:
            return False
    else:
        if input[midpoint] == target:
            return True
        elif input[midpoint] > target:
            return binary_search(front, target)
        elif input[midpoint] < target:
            return binary_search(back, target)

print(binary_search([1,2,3,4], 2)) # => True
print(binary_search([1,2,4,5], 3)) # => False
print(binary_search([4,53,150,76543], 53)) # => This exists at index 2