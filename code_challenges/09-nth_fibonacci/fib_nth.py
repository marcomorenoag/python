# Problem: https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1


def nth_fibonacci(n: int) -> int:
    c = 10**9 + 7
    fibonacci_generator = (
        a for a, b in [(0, 1)] for _ in range(n) for a, b in [(b, a + b % c)]
    )
    fibonacci_sequence = list(fibonacci_generator)
    return fibonacci_sequence[-1] % c


def nth_fibonacci_alt(n: int) -> int:
    mod = 10**9 + 7
    current, next = 0, 1
    for _ in range(n):
        yield current
        current, next = next, current + next


if __name__ == "__main__":
    print(nth_fibonacci(5))
