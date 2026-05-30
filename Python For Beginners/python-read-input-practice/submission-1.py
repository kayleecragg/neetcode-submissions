def add_two_numbers() -> int:
    myinput = input()
    myin = myinput.split(",")

    sum = 0
    for i in myin:
        sum += int(i)
    
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
