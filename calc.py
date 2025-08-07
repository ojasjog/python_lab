# You are using Python
num=int(input())
if num>9 or num<0:
    print("Invalid input")

calc=str(input())

if num>9 and num<0:
    print("Invalid input")

elif 0<=num<=9 and calc=='y':
    op=str(input())
    operand=int(input())
    if num>9 and num<0:
        print("Invalid input")
    else:
        if op=='*':
            k=num*operand
            print("The result of the operation is:", k)
        elif op=='+':
            l=num+operand
            print("The result of the operation is:", l)
        elif op=='-':
            m=num-operand
            print("The result of the operation is:", m)
        else:
            print("Invalid operation")
elif calc=='n':
    print(num)
