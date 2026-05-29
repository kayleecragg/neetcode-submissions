from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    mydict = {name: age}
    return mydict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    mydict = {}
    k = 0
    for i in words:
        mydict[i] = k
        k+=1
    
    return mydict



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
