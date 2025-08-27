
def is_prime(w):
    if w<2:
        return False
    for h in range(2, w):
        if w%h==0:
            return False
    return True
    
num = eval(input("Enter your number: "))
n=len(num)
k=list(num)
l=n-1
d=int("".join(map(str, k)))

print(d)

final_list=[]

if is_prime(d)==False:
    final_list.append(d)


for i in range(len(k)-1):
    l = l%n
    rotated = k[l:] + k[:l]
    c = int("".join(map(str, rotated)))
    print(c)
    
    i=i+1
    k=rotated
    if is_prime(c)==False:
        final_list.append(c)
        
if len(final_list)>0:
    print("false")
elif len(final_list)==0:
    print("true")
    
    
