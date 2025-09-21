
def insert_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0
    i = 0

    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i+1] == "_"):
                if i + 1 < len(txt):  
                    result += txt[i+1] + "_"
                    i += 1
            else:
                result += "_"
            count = 0
        i += 1

    if result.endswith("_"):
        result = result[:-1]

    return result
n = int(input())

for i in range(n):
    print(i ** 2)

i=1
while i in range (1,11):
    print (i)
    i+=1
for i in range (1,6):
    for j in range (1,i+1):
        print (f'{j}', end=' ')
    print ('')
number = int(input('Введите любое число'))
summa = 0
for i in range (1,number+1):
    summa +=i
print(summa)
number = int(input('Введите любое число'))

for i in range (1,11):
    print(i*number)
    i+=1
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers and (75,150,145):
    print (i)
number = input('Enter a number')
counter=0

for i in number:
    counter+=1
print (counter)
n = 5
for i in range(n, 0, -1):       
    for j in range(i, 0, -1):    
        print(j, end=" ")
    print()
