import re

#part 1


def count_letters(text_str):
    text = ""
    dic_count = {}
    for i in text_str:
        #remove unwanted characters
        i = i.lower()
        i = i.strip(" .,'!\n->;@?:#")
        text = text + i
        if i != '':
            # count the number of times we have the letter
            count = dic_count.get(i, 0)
            count += 1
            dic_count[i] = count
    return dic_count

def swap_dic(commonKeys,commonEnglishChars):
    #create a swap dict where the keys and the values are swapped
    final_dict = {}
    for value1, value2 in zip(commonKeys,commonEnglishChars):
        final_dict[value2] = value1
        final_dict[value1] = value2
    return final_dict

with open('original.txt', 'w') as file:
    file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.\n")
    file.write('J.U.U.U Kmltin.\n')
    file.write('mmps iks nmk eio; ---> hkmu\n')
with open('original.txt', 'r') as file:
    inputString = file.read()

text_count = count_letters(inputString)
# sorting the letter count in the dictionary according to their occurrences from smaller to bigger
text_count1 = sorted(text_count.items(), key=lambda x: x[1])
flip_list = text_count1[::-1]
# flip the list to get the higher occurrences first
high4 = flip_list[0:4]
# git the higher 4 occurrences
dict4 = dict(high4)
# turn into a dictionary
commonKeys = list(dict4.keys())
commonEnglishChars = ['e', 't', 'o', 'r']

final_dict = swap_dic(commonKeys, commonEnglishChars)
print('final dictionary:',final_dict)


#part 2
#go over all the letters in a file
letters_dict = final_dict
file = inputString
encrypted =""
for letter in file:
    if letter in letters_dict:
    #if the letter is in the dict swap it and add it to encrypted
        encrypted += letters_dict[letter]
    else:
    #if not add it to encrypted without swap
        encrypted += letter
print(encrypted)
encrypted_text = encrypted

#part 3
# create new file that includes the original string and the translation
with open('translated.txt', 'w') as file2:
    file2.write(inputString)
    file2.write("The encryption for the above text is: \n")
    file2.write(encrypted_text)
# Open a file with access mode 'w'
with open('Result.txt', 'w') as file1:
    # write 'decrypted_text' at the end of file
    file1.write(encrypted_text)

#part 4
#finding the longest word
import re
# Opening the given file in read mode.
with open('Result.txt', 'r') as file1:
# Getting the list of words of a file and removing all special char
    words_list = file1.read().split()
    strip_list =[re.sub('[^a-zA-Z0-9]+', '', _) for _ in words_list]
# the length of the word
    word_length = len(max(strip_list, key=len))
# looking for a word that has the same length as word_length
    longest_word = [word for word in strip_list if len(word) == word_length]
print("the longest word is:", longest_word)
file1.close()
#counting the lines
def count_lines(file1):
    with open('Result.txt') as file1:
        count = 0
        file1.seek(0)
        for line in file1:
            if line != "\n":
                count += 1
    return count
print('Total Lines:', count_lines(file1))
#print the longest word as much as the number of lines
x = str(longest_word)
y = count_lines(file1)
print(x*y)
#make a nested loop with x shape
i = 0
number_of_rows = 7
for row in range(7):
    for col in range(7):
        if row == i or col == number_of_rows:
            print("*",end = "")
            i = i + 1
            number_of_rows = number_of_rows - 1
        elif row == col :\
                 print("*",end = "")
        else:
            print(end = " ")
    print()
#part 5