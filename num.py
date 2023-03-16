n = int(input("Enter a number"))
sume = n % 2 
if sume==0 :
    if sume >= 2 and sume <= 5:
        print("Not Wired")
    elif sume >= 6 and sume <= 20:
        print("Wired")
    else:
        print("Not Wiered")
else:
    print("Wiered")