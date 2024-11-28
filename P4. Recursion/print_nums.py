
def print_nums(count)->int:
    if count>=10:
        return
    print(count)
    print_nums(count+1)


print_nums(0)


def fun(n):
    if n<=0:
        return
    
    print(n)
    fun(n-1)

fun(10)    