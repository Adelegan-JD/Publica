sentence = input("Please enter a sentence of your choice:")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
total_vowels = sum(1 for word in sentence if word in vowels)
print(total_vowels)