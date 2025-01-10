
# This module is about prime numbers. Use it if you feel like it.


def is_prime_number(number):
    lst = []
    for i in range(1, number + 1):
        if number % i == 0:
            lst.append(i)
    if len(lst) == 2:
        return True
    else:
        return False


def prime_numbers(start, end):
    primes = []
    for i in range(start, end + 1):
        if is_prime_number(i):
            primes.append(i)
        else:
            pass
    return primes
    
    
def total_primes(start, end):
    primes = prime_numbers(start, end)
    return len(primes)
    

def detailed_primes(entry = 100):
    constant = entry
    high = entry
    low = 0
    while low < constant:
        if high > 99:
            print(f"Total Prime Numbers ({low} - {low + 99}):   ", total_primes(low, low + 99))
            low += 100
            high -= 100
        else:
            print(f"Total Prime Numbers ({low} - {constant}): ", total_primes(low, constant))
            break
