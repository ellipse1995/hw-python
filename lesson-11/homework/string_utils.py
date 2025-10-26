def reverse_string(word):
    return word[::-1]

def count_vowels(word):
    vowel = "aeiouy"
    count = 0
    for i in word.lower():
        if i in vowel:
            count+=1
    return count

print(reverse_string("asror"))