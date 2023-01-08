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
            #return the value of the item with the specific key i
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

# a dictionary that shows how many times each letter appears
text_count = count_letters(inputString)
# sorting the items of the dictionary according to their occurrences from smaller to bigger in a list
text_count1 = sorted(text_count.items(), key=lambda x: x[1])
# flip the list to get the higher occurrences first
flip_list = text_count1[::-1]
# git the higher 4 occurrences
high4 = flip_list[0:4]
# turn into a dictionary
dict4 = dict(high4)
# make a list of the 4 most common keys from our file
commonKeys = list(dict4.keys())
# the given list
commonEnglishChars = ['e', 't', 'o', 'r']
# use the swap func to create a dictionary that includes swapped keys and values
final_dict = swap_dic(commonKeys, commonEnglishChars)
print('final dictionary:',final_dict)


# part 2
# translate the file
# the dictionary that we created in part 1
letters_dict = final_dict
# the file that we need to translate
file = inputString
# create an empty string that will be updated with the translation
encrypted =""
# go over each letter
for letter in file:
    if letter in letters_dict:
    # if the letter is in the dict, swap it and add it to the empty string
        encrypted += letters_dict[letter]
    else:
    # if not add it to empty string without swap
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

# part 4
# finding the longest word
# Opening the given file in read mode.
with open('Result.txt', 'r') as file1:
# getting the list of words of a file and removing all special char
    words_list = file1.read().split()
    strip_list =[re.sub('[^a-zA-Z0-9]+', '', _) for _ in words_list]
# get the length of the longest word ,output=10
    word_length = len(max(strip_list, key=len))
# looking for a word that has the same length as word_length
    longest_word = [word for word in strip_list if len(word) == word_length]
print("the longest word is:", longest_word)
file1.close()
#counting the lines
def count_lines(file1):
    with open('Result.txt') as file1:
        # count set to 0
        count = 0
        # get to the first line
        file1.seek(0)
        for line in file1:
            if line != "\n":
                count += 1
    return count

print ('Total Lines:', count_lines (file1))

# print the longest word as much as the number of lines
x = str(longest_word)
y = count_lines(file1)
print(x*y)
#make a nested loop with x shape
result_str="";
# go over the 7(from 0 to 6) rows one by one horizontally
for row in range(0,7):
    # go over the 5 columns vertically
    for column in range(0,7):
        # print the first two and last two lines the fall at the first and last columns at rows 1,2 & 5,6
        if (((column == 1 or column == 5) and (row > 4 or row < 2))
                # print the middle line where the column and raw fall at 3 ignore 0 and 6
                or row == column and column > 0 and column < 6
                # print line 2 and 4 the fall at column 2 row 4 and column 4 raw 2
                or (column == 2 and row == 4) or (column == 4 and row == 2)):
            result_str=result_str+"*"
        else:
            # if doesn't fulfill requirements print space
            result_str=result_str+" "
            # start a new line after each command
    result_str=result_str+"\n"
print(result_str)
#part 5