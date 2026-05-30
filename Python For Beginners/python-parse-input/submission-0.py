from typing import List

def read_integers() -> List[int]:
    inp = input()
    integers = inp.split(",")
    mylist = []

    for i in integers:
        mylist.append(int(i))

    return mylist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
