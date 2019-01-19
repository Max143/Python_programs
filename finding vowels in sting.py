# program to count the number of each vowel

vowels = 'aeiou'

ashi = input("Enter the string here: ")

ashi = ashi.casefold()

count = {}.fromkeys(vowels, 0)

for char in ashi:
    if char in count:
        count[char] += 1

print(count)
