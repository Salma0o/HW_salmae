import re
# Opening the given file in read mode.
with open('Result.txt', 'r') as file1:
# Getting the list of words of a file and removing all special char
    words_list = file1.read().split()
    strip_list =[re.sub('[^a-zA-Z0-9]+', '', _) for _ in words_list]
# the length of the word
    word_length = len(max(strip_list, key=len))
# looking for a word that has the same length as word_length
    result = [textword for textword in strip_list if len(textword) == word_length]
print("the longest word is:",result)
file1.close()
