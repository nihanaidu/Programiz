# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

for char in vowels:
    count=ip_str.count(char)
    print("Count of ",char," is ",count)
    count=0