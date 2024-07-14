def print_fibonacci(length):
    if length == 0:
        print("[]")
        return

    fib_sequence = [0, 1]
    
    if length == 1:
        print([0])
        return
    
    if length == 2:
        print(fib_sequence)
        return
    
    for i in range(2, length):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    print(fib_sequence)

# Test cases
print("Length 0:")
print_fibonacci(0)

print("\nLength 1:")
print_fibonacci(1)

print("\nLength 2:")
print_fibonacci(2)

print("\nLength 10:")
print_fibonacci(10)