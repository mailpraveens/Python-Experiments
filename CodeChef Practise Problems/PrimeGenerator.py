#using sieve of erasthrones

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]


    #to get input from command line - Woof that was an effort
if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            val = sieve_for_primes_to(10000);
            print("Hello")
        except:
            break