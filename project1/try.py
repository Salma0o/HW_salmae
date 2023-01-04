



print('part 4')  #part 4






#count lines in result file
def count_lines(file1):
    with open('Result.txt') as file1:
        count = 0
        file1.seek(0)
        for line in file1:
            if line != "\n":
                count += 1
    return count
print('Total Lines:', count_lines(file1))

print('part5') #part 5
#readme design




