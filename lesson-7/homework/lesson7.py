def is_prime(n):
    int(n)
    if n<1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i == 0:
            return False
    else:
        return True

    
def digit_sum(k):
    sum=0
    for i in str(k):
        sum += int(i)
    return sum


def power_of_two(n):

    for i in range (1,n+1):
        if 2**i<=n:
            print (2**i, end=" ")


