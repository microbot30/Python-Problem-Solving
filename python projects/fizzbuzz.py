def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    elif n % 3 == 0:
        return "FIZZ"
    elif n % 5 == 0:
        return "BUZZ"
    else:
        return str(n)


for i in range(1, 101):
    print(fizzbuzz(i), end=' ')
