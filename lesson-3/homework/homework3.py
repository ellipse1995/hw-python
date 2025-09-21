fruit = ['apple', 'banana', 'peach', 'orange', 'melon']
print (fruit[2])
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
print (list1+list2)
numbers = [1,6,7,21,77,21,17]

print ('First number', numbers[0])
print ('Middle number', numbers[len(numbers) // 2])
print ('Last number', numbers[-1])
newlist = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Gladiator"]

tuple_movies = tuple(movies)
print (tuple_movies)
cities = ["London", "New York", "Paris", "Tokyo", "Berlin"]
cities_lower = [city.lower() for city in cities]
if 'paris' in cities_lower:
    print ('Paris in the list')
else:
    print ('Not found')
numbers = [1,6,7,21,77,21,17]
duplicate = numbers.copy()
numbers = [1,6,7,21,77,21,17]
new_numbers = [numbers[-1]] + numbers[1:-1]+[numbers[0]]

print (new_numbers)
numbers = tuple(range(1, 11))
slice_part = numbers[3:8]

print(slice_part)
colors = ["red", "blue", "green", "blue", "yellow", "blue"]

print (colors.count('blue'))

animals = ("tiger", "elephant", "lion", "giraffe", "zebra")

print (animals.index('lion'))
tuple1=(1,2,3,5,6)
tuple2= (7,8,9,10)
merged = tuple1 + tuple2

print(merged)

listt = [10, 20, 30, 40, 50]
tuplee = (1, 2, 3, 4)

print (f"Length of the list is {len(listt)}, and length of the tuple is {len(tuplee)}")
numbers_tuple = (10, 20, 30, 40, 50)
listt= list(numbers_tuple)

print (listt)

words = ("apple", "banana", "cherry", "date", "fig")

print (words[::-1])
