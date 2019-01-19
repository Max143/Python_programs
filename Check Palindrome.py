'''
Check Palindrome

'''

# Palindorme means word == reverse.word ex- TIT = TiT, Tip != piT


user_input = input("Enter the Word: ")

rev_word = user_input[::-1]

# print(rev_word) Will print reverse of user_input

def main():
    if user_input == rev_word:
        print("Your word is a Palindrome.")
    else:
        print("your word is not Palindorme.")
        
main()


    
