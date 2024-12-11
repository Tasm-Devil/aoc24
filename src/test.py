def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = int(input("Wie viele Fibonacci-Zahlen möchten Sie sehen? "))
    fib_sequence = fibonacci(n)
    print(f"Die ersten {n} Fibonacci-Zahlen sind: {fib_sequence}")

if __name__ == "__main__":
    main()