def reverse(input):
    if input.next == null:
        return input
    input.next.next = input
    reverse(input.next)

node1 = {
    next: node2,
    value: 1
}

node2 = {
    next: node3,
    value: 2
}

node3 = {
    next: null,
    value: 3
}

node3.next = node2
node2.next = node1

# node1 represents the entire array