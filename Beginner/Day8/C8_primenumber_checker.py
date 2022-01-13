def prime_checker(number):
    num_devisions = 0
    for i in range(2, number):
        if number % i == 0:
            num_devisions += 1
    if num_devisions > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
