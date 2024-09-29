import random

def generate_keypair(p, q):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    phi = (p-1) * (q-1)

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    while True:
        e = random.randrange(1, phi)
        if is_prime(e):
            if e < phi:
                if gcd(e, phi) == 1:
                    break
    def multiplicative_inverse(e, phi):
        d = 1
        while (d * e) % phi != 1:
            d += 1
        return d

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
