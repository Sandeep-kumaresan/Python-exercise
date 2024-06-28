inp=input("Enter String: ")
if inp.isalnum() == True and inp.isalpha()== False and inp.isdigit() == False:
    print(True)
else:
    print(False)