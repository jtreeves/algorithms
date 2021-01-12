def merge(set1, set2):
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

def split(input):
    midpoint = len(input) // 2
    set1 = input[:midpoint]
    set2 = input[midpoint:]
    if len(set1) <= 1 and len(set2) <= 1:
        return merge(set1, set2)    
    split_set1 = split(set1)
    split_set2 = split(set2)
    return merge(split_set1, split_set2)

print(split([2, 3, 1, 7, 4, 5]))