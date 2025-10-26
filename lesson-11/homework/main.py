from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Математика
print("add(2, 3) =", add(2, 3))
print("subtract(10, 4) =", subtract(10, 4))
print("multiply(6, 7) =", multiply(6, 7))
print("divide(20, 5) =", divide(20, 5))

# Строки
word = "Hello, Привет!"
print("reverse_string:", reverse_string(word))
print("count_vowels:", count_vowels(word))

# Геометрия
r = 5
print("Circle area:", calculate_area(5))
print("Circle circumference:", calculate_circumference(5))

# Файлы
write_file("sample.txt", "Строка 1\nСтрока 2\nПривет, файл!")
print("Файл прочитан:\n" + read_file("sample.txt"))