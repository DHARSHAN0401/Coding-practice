#Q4 string is an anagram :

def is_anagram(str1, str2):
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

    # Inputs
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
