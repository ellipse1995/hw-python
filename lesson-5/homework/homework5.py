

def leap_year(year):
    
    return year%4 == 0 and (year%100 != 0 or year%400==0)
        

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
#solution 2
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
start = a+ (a%2)
evens = list(range (start,b+1,2))

print (evens)
