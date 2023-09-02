def print_operation_table(op, x, y):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(op(i, j), end=" ")
        print()


print_operation_table(lambda x, y: x * y, 6, 6)
