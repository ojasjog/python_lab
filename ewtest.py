import math
from math import e


e1=eval(input("Enter E value: "))
y=eval(input("Enter gamma: "))

if y==0.570:
    
    

    enot=e1-((0.0595/2)*math.log(y*0.05, 10))
    print(enot)

elif y==0.485:
    enot=e1-((0.0595/2)*math.log(y*0.1, 10))
    print(enot)





