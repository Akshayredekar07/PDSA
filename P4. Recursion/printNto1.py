
def printrev(i: int, n: int)->int:

    if(i>n):
        return
    
    printrev(i+1, n)
    print(i)

printrev(1, 5)    



# def printNto1(i ,N):
#     if i < 1:
#         return
    
#     print(i)
#     printNto1(i-1, N)


# if __name__ == "__main__":
#     printNto1(5,5)