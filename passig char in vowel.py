# TEST WHEATHER A PASSED LETTER IS A VOWEL OR NOT

def  is_vowel(char):
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    
    
    if char in vowel:
        print("Vowel")
    elif char in consonant:
        print("consonant")
    else:
        print("None")
    


print(is_vowel('a'))

