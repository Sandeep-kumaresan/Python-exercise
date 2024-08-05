
def plusOne(digits):

    sam="".join(map(str,digits))
    inc=int(sam)+1
    dig=[int(i) for i in str(inc)]
    return dig
digits = [4,3,2,1]
print(plusOne(digits))