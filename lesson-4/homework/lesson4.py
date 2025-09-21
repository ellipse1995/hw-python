#1
my_dict = {"apple": 10, "banana": 2, "cherry": 15, "date": 7}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)

#2
my_dict = {"apple": 10, "banana": 5}

my_dict["cherry"] = 15

print(my_dict)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}

print( result)


#4
n = int(input("Enter a number: "))

squares = {x: x*x for x in range(1, n+1)}

print(squares)

#5
square = {x: x*x for x in range (1,16)}
print (square)

#6
my_set = {1, 2, 3, 4, 5}

print (my_set)


#7
my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print (i)

#8
numbers = {1, 2, 3}
numbers.add(4)
print("After adding one number:", numbers)
numbers.update([5, 6, 7])
print("After adding a list of numbers:", numbers)

#9
numbers = {1, 2, 3, 4, 5, 6}

for i in (1,2,5):
    numbers.remove(i)
    print ('Deleted ',i)
print ('Set at the end:',numbers)
numbers = {1, 2, 3, 4, 5}

#10
numbers.discard(7)



