# primality test 2, modified code snippet from geeksforgeeks.org
import time

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 


    prime = [True for i in range(n+1)] 
    p = 2
    count = 0
    while (p * p <= n):        
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False              
        p += 1
    with open("primes.txt", "w") as txt:
        count = 0
        for x in range(2, n):
            if prime[x]:
                count += 1
                txt.write(f"N = {count} : P = {x} : Percent Prime - {((count/x)*100):5.3} %\n")
      
  
if __name__=='__main__': 
    start = time.process_time()
    n = 17000000
    print("Following are the prime numbers smaller")
    print ("than or equal to", n) 
    SieveOfEratosthenes(n) 
    print(f"Time for completion: {time.process_time() - start}")

    