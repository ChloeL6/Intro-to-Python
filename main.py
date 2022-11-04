
#%%
list_test = ["there", "is", "a", "bird"]
empty_list= []

def list_sayer(list):
    if len(list) != 0:
        for index in range(len(list)):
            print(f'the item name is {list[index]}, and its index is {index}')
        result = True
    else:
        print("List is empty")
        result = False
    return result

list_sayer(list_test)


# %%
dict_test = { "hi": 2, "tea": 3, "cloud": 4}
empty_dict = {}

def dict_sayer(dict_test):
    if len(dict_test) != 0:
        for k, v in dict_test.items():
            print(f'item key is {k}, its value is {v}')
        result = True
    else:
        print("Dictionary is empty")
        result = False
    return result

dict_sayer(empty_dict)


#%%
more_dict = {tuple(["salt", "pepper"]): 9, tuple(["pepper", "chili"]): 99, tuple(["oil", "peanut"]): 999 }

greatest_value = float('-inf')
same_key = ""
def greatest(more_dict) :
    for k,v in more_dict.items():
        if v > greatest_value:
            greatest_value = v
            same_key = k
    return (greatest_value, same_key)

greatest(more_dict)


#%%
test_1 = ["this", "is", "list", "one"]
test_2 = ["list", "two", "equal", "two"] 
test_3 = ["here", "is", "list", "three", "but", "longer"]

result = {}
new_dict = {}
emp_list = []
def zipper(list1, list2):
    if len(list1) == len(list2):
        for item1 in list1:
            for item2 in list2:
                new_dict[item1] = item2
                list2.remove(item2)
                break
        result = new_dict
    elif len(list1) != len(list2):
        emp_list.append(list1)
        emp_list.append(len(list1))
        emp_list.append(list2)
        emp_list.append(len(list2))
        result = tuple(emp_list)               
    return result
    
zipper(test_1, test_3)