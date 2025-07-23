'''Now I'll start with the Exercises no.2'''

#Exercise no.1 Write a function to count the number of vowels in a given string :

#task 1:
'''def count_vowels(My_TXT): #this function will return the number of vowels u used in a text
    Count = 0
    english_vowels = "aioueAIOUE"
    for char in english_vowels:
        if char in My_TXT:
            Count +=1
    return Count
My_TXT = input("enter a text")
print(f"this is ur number of vowels in the txt u wrote {count_vowels(My_TXT)}\n")

#Task 2:
def apper_second_letter(My_TXT_2): #this function will return every text u enter by capitalized every secound char
    After_Capitalized = ""
    for i in range(len(My_TXT_2)):
        if i % 2 == 1:
            After_Capitalized += My_TXT_2[i].upper()
        else:
            After_Capitalized += My_TXT_2[i]
    return After_Capitalized

My_TXT_2 = input("input a text pls")
print(f"ur Text after capitalized secound latter will be like this: {apper_second_letter(My_TXT_2)}\n")

#Task 3:

a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
even_list =[]
odd_list = []
for num in range(a_list): #this code will return the even number by a list
    if num %2 == 0 :
        even_list.append
    else:
        odd_list.append
print(f"this is ur even nums:{even_list}\n")
print(f"this is ur odd nums:{odd_list}\n") # I don't know why I have an error boss I'm so so sad :(

#task 4:
lst_of_numbers = [1,2,3,4,5,6,5,7,8,3,1,5,2,7,8,8,4,5]
uniqe_list = []
uniqe_list = set(lst_of_numbers) #set will remove the duplicates
print(f"This is ur list after removing duplicates:{uniqe_list}\n")

#task 5 and task 6: #2 in 1 ;) 

def intersection_sets(set1,set2):
    return  set1 & set2
def union_sets(set3,set4):
    return set3 | set4 
ur_set1={1,2,3,4,56,7,8,9}
ur_set2={1,2,3,4,7,89,6,4}
print(f"here is ur intersection number between this two sets:{intersection_sets(ur_set1,ur_set2)}\n") # this will retur the intersection numbers between sets
print(f"here is ur union number between this two sets:{union_sets(ur_set1,ur_set2)}\n") # this will return the union number between the sets

#task 7:

def sort(tuples_list): #this will sort the tuple by the secound number
    return sorted(tuples_list, key=lambda  i: i[1]) #lumbda tells the function to take or return the second number
items = [(6,5,8),(9,3,6),(8,2,100)]
print(f"this is ur sorted number by secund element:{sort(items)}\n")

#task 8:

def reversed_tuple(any_tuple):
    return any_tuple[::-1] #this function will return any tuple reversed

my_tuple=(1,2,3,456,34,76,231,46546757,4354545,4545221,7689767,9)
print(f"this is ur tuple reversed:{reversed_tuple(my_tuple)}\n") 

#task 9:

def separate(any_dictionary):#this function will return ur dictionare but seperat the values and keys
    my_keys = list(any_dictionary.keys())
    my_values = list(any_dictionary.values())
    return my_keys, my_values
my_dictionary = {"mohammad":22,"Lujain":15,"Abood":15,"Yousef":13}

print(f"this is ur dictionary but seperated the values and keys{separate(my_dictionary)}\n")

#task 10:

def get_value(dictionary, key, default_value=None):
    return dictionary.get(key, default_value)
my_dictionary2 = {"mohammad":22,"Lujain":15,"Abood":15,"Yousef":13}

print(get_value(my_dictionary2,'mohammad','none'))
print(get_value(my_dictionary2,'Lujain','none'))'''
