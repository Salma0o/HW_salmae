import math

#a function that counts words on file and returns a dict
def word_count(file_path):
    #open empty dict
    counts = dict()
    #open the file in write and read mood
    with open("my_id.txt", "w+") as file:
        file.write("my name is salma\n")
        file.write("I enjoy the cold weather\n")
        file.write("I am 27 years old\n")
        #return to first line
        file.seek(0)
        #split the file to words
        words=file.read()
        #for each word in words
        for word in words.split():
            #if word is in the empty dict add 1
            if word in counts:
                counts[word] += 1
                #if not, add nothing
            else:
                counts[word] = 1

    return counts

print( word_count("my_id.txt"))
#{'my': 1, 'name': 1, 'is': 1, 'salma': 1, 'I': 2, 'enjoy': 1, 'the': 1, 'cold': 1, 'weather': 1, 'am': 1, '27': 1, 'years': 1, 'old': 1}

# a function that will print the first line in file
#open file in read mood
with open("my_id.txt", 'r') as file:
    #choose the number of lines you want to print
    n = 3
    #read the lines in a file one by one
    lines_in_file= file.readlines()
    #for each line in the lines go over the lines n
    for line in (lines_in_file[:n]):
        #print that line
        print(line)

with open('my_id.txt', 'r') as file:
# getting the list of words of a file
    words_list = file.read().split()
# get the length of the longest word
    word_length = len(max(words_list, key=len))
# looking for a word that has the same length as word_length
    longest_word = [word for word in words_list if len(word) == word_length]
print("the longest word is:", longest_word)
file.close()
#a function that reverse a file
def reverse(file_path):
    #open file in read mood
    with open("my_id.txt", 'r') as file:
        #skip to first line
        file.seek(0)
        #split the world and create a list then flip it
        word_list = file.read().split()[::-1]
    #return the joined words from the list as a string
    return(" ".join(word_list))
print(reverse("my_id.txt"))




class shout_string:
    def __init__(self,string1):
        self.string1 = string1
    def get_string(self):
        self.string1 = input()
    def print_string(self):
        print(self.string1.upper())
str1 = shout_string("hello world")
print(str1.print_string())


#a class that give the rectangle area
class Rectangle:
    name = "Rectangle"
    def __init__(self, width, height):
        if ((type(width) is int or type(width) is float) and \
                (type(height) is int or type(height) is float )) \
                and width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise TypeError("The values must be positive numbers")

    def area(self):
        return self.height * self.width
r1 = Rectangle(4,5)
print(r1.area())






