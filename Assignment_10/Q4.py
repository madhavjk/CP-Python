
parent = input()
Yes_No = input()
if Yes_No == "N":
    print("TOTAL MEMBERS:1\nCOMMISSION DETAILS\n{0}: 250 INR".format(parent))
elif Yes_No == "Y":
    child=list(map(str,input().split(",")))
    print("TOTAL MEMBERS:{}".format(len(child)+1))
    print("COMMISSION DETAILS \n{0}:{1} INR".format(parent,len(child)*500))
    for i in child:
        print("{0}:250 INR".format(i))