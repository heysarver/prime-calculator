import argparse
import math

def sieve_of_eratosthenes(limit):
    """Use the Sieve of Eratosthenes to find all prime numbers up to a given limit."""
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

def main():
    parser = argparse.ArgumentParser(description="Calculate prime numbers up to a limit.")
    parser.add_argument("--limit", type=int, required=True, help="The upper limit up to which to calculate prime numbers.")
    parser.add_argument("--print-primes", action="store_true", help="Print the prime numbers.")

    args = parser.parse_args()

    primes = sieve_of_eratosthenes(args.limit)
    num_primes = len(primes)

    print(f"Number of primes up to {args.limit}: {num_primes}")

    if args.print_primes:
        print("Prime numbers:", primes)

if __name__ == "__main__":
    main()
