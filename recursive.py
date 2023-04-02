def fibonacci(current, last, limit):
    print(current)
    last, current = current, current + last
    if current <= limit:
        fibonacci(current, last, limit)

toprint = fibonacci(1, 0, int(input("what's the limit")))
toprint