

from narwhals import when


def gen_values():
    yield 1
    yield 2
    yield 3

gen_values_obj = gen_values()
# we have a generator object that we can iterate over or we can use the next() function to get the next value from the generator object
print(gen_values_obj) # <generator object gen_values at 0x000001B9C8F1E5C0>
print(next(gen_values_obj)) # 1
print(next(gen_values_obj)) # 2
print(next(gen_values_obj)) # 3
# print(next(gen_values_obj)) # StopIteration error because there are no more values to yield

print("\n")
print("Iterating over the generator object using a for loop")
# eaiser way to iterate over the generator object is to use a for loop
for value in gen_values():
    print(value)

# when these generators are useful? 
# when we have a large dataset and we want to process it in chunks instead of loading the entire dataset into memory at once.
# This is where generators come in handy because they allow us to generate values on the fly and only keep the current value in memory. 
# This is especially useful when working with large files or when we want to create an infinite sequence of values.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
# Using the generator
for number in count_up_to(5):
    print(number)

# Example showing prime numbers using generators and not using generators


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_list(start, end):
    """Eagerly compute and return a list of primes in [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def gen_primes(start, end):
    """Lazily yield primes in [start, end]."""
    for num in range(start, end + 1):
        if is_prime(num):
            yield num


print("\nPrimes using eager list:")
primes = get_primes_list(50, 100)
print(primes)

print("\nPrimes using generator (lazy):")
g = gen_primes(50, 100)
# show first two items with next()
print(next(g))  # 53
print(next(g))  # 59
# continue iterating from where we left off
print("Remaining primes from generator:")
for p in g:
    print(p, end=" ")
print()
