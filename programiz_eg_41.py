# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

words = my_str.split()
sorted_words=sorted(words,key=str.lower)
for word in sorted_words:
    print(word)