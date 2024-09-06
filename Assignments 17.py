




def find_common_elements(list1,list2):
    common_elements = list(set(list1)& set(list2))
    return common_elements

lista = [1, 2 , 3, 4 , 5]
listb = [4, 5, 6, 7, 8]

result  = find_common_elements(lista,listb)
print("Common Elements:", result )