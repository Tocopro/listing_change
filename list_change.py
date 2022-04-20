# substitution

def sub_element():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    a = list1.index(25)
    print(a)
    list1[a] = 200
    print(list1)
    lb = list1.index(5)
    list1[lb] = 0
    print(list1)


sub_element()
