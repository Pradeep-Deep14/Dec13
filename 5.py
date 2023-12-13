from collections import Counter

def get_peter(data:list):
    count_peter=Counter(data).get("peter")
    if not count_peter:
        results="He is missing"
    else:
        results=count_peter
    
    return results

list1=['John','Kelly','Peter','Moses','Peter']

print(get_peter(list1))