def primeCheck(num):
    dividend = num//2
    for i in range(2,dividend+1):
        if num % i == 0:
            return False
        return True
    

n = int(input("Enter a number range to check prime: "))
print([x for x in range(1,n) if primeCheck(x)])