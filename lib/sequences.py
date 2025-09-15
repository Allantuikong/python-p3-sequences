def print_fibonacci(length):
    # Handle edge cases
    if length == 0:
        fib_sequence = []
    elif length == 1:
        fib_sequence = [0]
    else:
        # Initialize the list with the first two Fibonacci numbers
        fib_sequence = [0, 1]
        
        # Generate Fibonacci numbers until we reach the desired length
        while len(fib_sequence) < length:
            # Add next Fibonacci number (sum of last two numbers)
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
    
    # Print and return the sequence
    print(fib_sequence)
    return fib_sequence