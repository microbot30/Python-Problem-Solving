def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FIZZBUZZ"
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 == 0:
        return "BUZZ"
    return str(n)


for i in range(1, 101):
    print(fizzbuzz(i), end=' ')
