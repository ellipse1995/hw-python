try: 
    a = int(input("Введите первое число"))
    b = int(input("Введите второе число"))
    c = a/b
    print(c)

except ZeroDivisionError:
    print("Делить на ноль нельзя!")
try:
    inp = input("Введите число")
    number = int(inp)
except ValueError:
    print("Вы ввели не число")
try:
    with open ("test.txt", "r") as test:
        content = test.read()
        print(content)
except FileNotFoundError as filerror:
    print("Файл не найден")

a = input("Первое число")
b = input("Второе число")

def is_digit(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

if not (is_digit(b) and is_digit(a)):
    raise TypeError("Вы ввели не числа")



try: 
    with open("example.txt", "r") as example:
        example.write("asd")
except PermissionError:
    print("Недостаточно прав для записи")
number = [1,2,3,4,5]

try:
    index = int(input("Введите индекс списка для вывода"))
    print (f'{index} ый индекс списка равен: {number[index]}')
except IndexError:
    print("Неверный индекс списка")
try:
    a = input("Введите слово")
    print ("вы ввели: ",a)
except KeyboardInterrupt:
    print("Пользователь прервал ввод")
try:
    with open ("outline.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print (content)
except UnicodeEncodeError:
    print("Ошибка в unicode файла")    

numbers = [1,23,4,5,6,7]

try:
    numbers.apend("a")
except AttributeError:
    print("Неверный атрибут")
with open ("python11/lesson12/outline.txt", "r") as file:
    content = file.read()
    print (content)
with open ("python11/lesson12/outline.txt", "r") as file:
    content = file.readlines()
    for i in content[0:2]:
        print (i, end="")
with open ("python11/lesson12/outline.txt", "w") as file:
    file.write("Test 2")
        
with open ("python11/lesson12/outline.txt", "r") as file:
    content = file.readlines()
    n = int(input("введите число строк"))
    for i in content[-n:]:
        print (i, end="")

#Write a Python program to read a file line by line and store it into a list.


filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    lines = file.readlines()

print(lines)
# Write a Python program to read a file line by line and store it into a variable.

filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    data = file.read()

print(data)

filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    array = file.readlines() 

print(array)
with open("python11/lesson12/outline.txt", "r") as file:
    words = file.read().split()        # читаем всё и разбиваем по пробелам
    print(max(words, key=len))
    
        


with open("python11/lesson12/outline.txt", "r") as file:
    words = file.readlines()
    print(len(words))
#Write a Python program to count the frequency of words in a file.

with open("python11/lesson12/outline.txt", "r") as file:
    words = file.read().split()
    chastota = {}
    for i in words:
        if i in chastota:
            chastota[i] +=1
        else:
            chastota[i] = 1
    print(chastota)
with open("python11/lesson12/outline.txt", "r") as file:
    file.seek(0, 2)          # Move the cursor to the end of the file
    a = file.tell()       # Get the position of the cursor (file size in bytes)

source = input("Enter source filename: ")
destination = input("Enter destination filename: ")

with open(source, "r", encoding="utf-8") as src:
    data = src.read()

with open(destination, "w", encoding="utf-8") as dst:
    dst.write(data)

