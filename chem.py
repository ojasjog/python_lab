dg=eval(input("Enter deltaG: "))
t=313
dg1=eval(input("Enter lower dg: "))
dg2=eval(input("Enter higher dg: "))
dt=20
dh=dg-((t)*(dg1-dg2)/dt)

k=(dg1+dg2)/dt
print(k)

print(dh)

