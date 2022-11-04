# Another way to solve zipper(). use zip() instead of for loop

test_1 = ["this", "is", "list", "one"]
test_2 = ["list", "two", "equal", "two"] 
test_3 = ["here", "is", "list", "three", "but", "longer"]

result = {}
new_dict = {}
emp_list = []
def zipper(list1, list2):
    if len(list1) == len(list2):
           new_dict = dict(zip(list1, list2))
           result = new_dict
    elif len(list1) != len(list2):
        emp_list.append(list1)
        emp_list.append(len(list1))
        emp_list.append(list2)
        emp_list.append(len(list2))
        result = tuple(emp_list)               
    return result

zipper(test_1, test_3)
