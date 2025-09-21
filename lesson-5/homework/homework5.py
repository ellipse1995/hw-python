

def leap_year(year):
    
    if year%4 == 0 and (year%100 != 0 or year%400==0):
        print ('Это высокосный год')
    else: 
        print('Это не высокосный год')


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

evens = list(x for x in range (a,b+1) if not x%2)

print (evens)
