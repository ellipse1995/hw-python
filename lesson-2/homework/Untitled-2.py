# %%
#1. Age Calculator
#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input('Write your name')
year_of_birth = int(input('Wirte your year of birth'))
print(f'{name}, now you are {2025-year_of_birth} years old')

# %%
#2. Extract Car Names
#Extract car names from the following text:
#txt = 'LMaasleitbtui'
txt='LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

# %%
#3. Extract Car Names
#Extract car names from the following text:

#txt = 'MsaatmiazD'
txt = 'MsaatmiazD'
print(txt[::2])
print(txt[::-2])

# %%
#4. Extract Residence Area
#Extract the residence area from the following text:
#txt = "I'am John. I am from London"

txt = "I'am John. I am from London"
print('John is from', txt[txt.find("from")+5::])


# %%
#5. Reverse String
#Write a Python program that takes a user input string and prints it in reverse order.

inputtext = input('Введите любое слово, и оно выйдет в обратном порядке')
print(inputtext[::-1])


# %%
#6. Count Vowels
#Write a Python program that counts the number of vowels in a given string.

txt = input("Введите любое слово на латинице, программа посчитает гласные")
vowel = 'a,i,o,e,u'
vovel = vowel.split(',')
count = 0
for i in txt:
    if txt in vovel:
        count+=1
print(count)



# %%
#7. Find Maximum Value
#Write a Python program that takes a list of numbers as input and prints the maximum value.

listt = input('Введите лист цифр через пробел')
splitted = max(listt.split())
print (splitted)


# %%
#8. Check Palindrome
#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# %%
#9. Extract Email Domain
#Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Введите свой email")
print(email[email.find('@')+1::])

# %%
#10. Generate Random Password
#Write a Python program to generate a random password containing letters, digits, and special characters.


