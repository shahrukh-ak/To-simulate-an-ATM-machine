amount = int(input("Enter your amount to be drawn: "))
am_str = str(amount)
v=int(am_str[1])*10
if amount%5 == 0 and v%20==0:
    a = am_str[0]
    b = int(a) * 100
    if b%100 == 0:
        b = b//100
    c = am_str[1]
    d = int(c)*10
    if d%20 == 0:
        d=d//20
    e = am_str[2]
    f = int(e)
    if f == 5:
        f = f//5
    elif f == 0:
        f = "0"
    else:
        print("The amount can not be drawn")
    print(f"Please collect you bill as follows:\n $100: {b} \n $20: {d} \n $5: {f}")
    
else:
    print("The amount can not be drawn")
