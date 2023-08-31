## 2.1 A)

def count_unique_consonants(string): 
    unique_consonants = set()
    vowels = set("aeiou")

    for letter in string:
        if letter.isalpha() and letter not in vowels:
            unique_consonants.add(letter)

    return len(unique_consonants)

print(count_unique_consonants("cat"))        
print(count_unique_consonants("cataract"))  

## 2.1 B)

"""
The space and time complexity of my solution is O(n) where n is the length of the string.
"""
pass

## 2.2
def count_squares_in_grid(x):

    if x <= 1: return x * x
    return count_squares_in_grid(x - 1) + x * x

print(count_squares_in_grid(1))
print(count_squares_in_grid(2))
print(count_squares_in_grid(3))