def is_prime(n):
    prime = True
    for i in range(1,n):
        if n%i == 0:
            prime = False
    return prime
    
def absolute_value(n):
    if n < 0:
        return -n
    elif n > 0:
        return n
