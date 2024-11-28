
def print_one_to_n(i: int, n:int):
    if i>n:
        return 
     
    print(i)
    print_one_to_n(i+1, n)


print_one_to_n(1, 7)

