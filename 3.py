def append_to(element,to=[]):
    to.append(element)
    return to

list1=append_to(1)
list2=append_to(2,[])
list3=append_to(3)
print(list1,list2,list3)