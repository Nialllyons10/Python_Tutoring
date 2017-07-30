def sumPrimes(n):
    sum = 0
    sieve = [True] * (n+1)
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum
			   
			   
def main():
	print(sumPrimes(2000000))


if __name__ == "__main__":
   main()