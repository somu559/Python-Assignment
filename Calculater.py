class calculater:
    def add():
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        print(a+b)
    
    def sub():
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        print(a-b)
        
    def mul():
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        print(a*b)
        
    def div():
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        print(a/b)
        
operator=input("enter  a operator")
if operator=="+":
    res=calculater.add()
elif operator=="-":
    res=calculater.sub()
elif operator=="*":
    res=calculater.mul()
elif operator=="/":
    res=calculater.div()
else:
    print("Enter a valid operator")
