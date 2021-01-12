def merge_sort(set1, set2):
    output = []
    combined_start_lengths = len(set1) + len(set2)
    while len(output) < combined_start_lengths:
        if len(set1) == 0:
            output += set2
            set2 = []
        elif len(set2) == 0:
            output += set1
            set1 = []
        elif set1[0] < set2[0]:
            output.append(set1[0])
            set1 = set1[1:]
        else:
            output.append(set2[0])
            set2 = set2[1:]
    return output

print(merge_sort([2], [4])) # => [2, 4]
print(merge_sort([4], [2])) # => [2, 4]

# ALTERNATIVE WHILE LOOP
# while len(set1) > 0 or len(set2) > 0