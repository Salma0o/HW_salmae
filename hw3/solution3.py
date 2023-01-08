#Q1
d1 = {("name", "Last_name"):"Salma Eyadi", ("age"): 26, ("phone number"): "0527389001"}
print(d1)

#Q2

def list5 (list1) :
    try:
          list1[5] = '@'
    except  IndexError:
        return "your list has less than 6 items"
    else:
          return list1
print(list5(["car","fat","ugly","hard","dad","dad"]))

#Q3

def list5 (list1) :
    assert len(list1) > 5,"goodbye,list should be at least 6 items"
    list1[5] = '@'
    return list1

list1 = ["car","fat","ugly","hard","dad","back"]
print(list5(list1))

#Q4
def up_dic(dic1,key_value) :
        dic1.update({key_value})
        return dic1
dic1 = {1: "one", 2: "two"}
key_value = (3,"three")
print(up_dic(dic1,key_value))

#Q5
dict3 = {}
n = 5
for x in range(1,n+1):
    key_value = {x : x+3}
    dict3.update(key_value)
print(dict3)

#6
dic1= {1:10, 2:20}
dic2= {3:30, 4:40}
dic3= {5:50, 6:60}
dict4= {**dic1,**dic2,**dic3}
print("Expected Result :",dict4)

#7

def countfun(Input_string):
    count_dict = {}
    Input_string = Input_string.upper()
    for letter in Input_string:
        counter = count_dict.get(letter,0)
        counter +=1
        count_dict[letter] = counter
    return count_dict
Input_string = "hanna"
print(countfun(Input_string))
 #8
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d1:
    if key in d2:
        d1[key] = d1[key] + d2[key]
    else:
        pass
print("Counter",d1)

