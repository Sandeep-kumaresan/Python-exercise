mark=float(input("Enter mark: "))
if mark >90:
    print("O grade")
elif mark >80 and mark<90:
    print("A grade")
elif mark >70 and mark<80:
    print("B grade")
elif mark >60 and mark<70:
    print("C grade")
elif mark >=50 and mark<60:
    print("D grade")
else:
    print("Fail")