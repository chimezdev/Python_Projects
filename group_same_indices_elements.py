# given the following list
input_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# group the elements of the same indices to be in one list

index_0_elem = []
index_1_elem = []
index_2_elem = []

for elem in input_list:
    for i in elem:
        #print(elem)
        if i == elem[0]:
            index_0_elem.append(i)
        elif i == elem[1]:
            index_1_elem.append(i)
        else:
            index_2_elem.append(i)
            
print(index_0_elem, index_1_elem, index_2_elem)

