def sieve(limit):
    if limit < 2:
        return []
    res = [False] * (limit + 1)
    if limit >= 2:
        res[2] = True
    if limit >= 3:
        res[3] = True

    for i in range(4, limit + 1):
        res[i] = False

    i = 1
    while i * i <= limit:
        j = 1
        while j * j <= limit:
            n = (4 * i * i) + (j * j)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                res[n] ^= True

            n = (3 * i * i) + (j * j)
            if n <= limit and n % 12 == 7:
                res[n] ^= True

            n = (3 * i * i) - (j * j)
            if i > j and n <= limit and n % 12 == 11:
                res[n] ^= True

            j += 1
        i += 1

    r = 5
    while r * r <= limit:
        if res[r]:
            for i in range(r * r, limit + 1, r * r):
                res[i] = False
        r += 1

    return [i for i in range(limit + 1) if res[i]]


def pick_prime(primes, min_size=1000):
    for prime in primes:
        if prime >= min_size:
            return prime
    return primes[-1]


def hash(string, modulus):
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
    return hash_value % modulus


if __name__ == '__main__':
    primes = sieve(10000)
    modulus = pick_prime(primes, 1000)

    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]

    for string in test_array:
        hash_value = hash(string, modulus)
        print(f"Hash of {string} is {hash_value}")
