#Q21 count vowels, consonants and special char.

def count_vowels_consonants_special(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    special_count = 0
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i in vowels:
            vowel_count += 1
        elif i in consonants:
            consonant_count += 1
        else:
            special_count += 1
    
    return vowel_count, consonant_count, special_count

#call function:
s=input("enter the sentenses:")
print(count_vowels_consonants_special(s))

