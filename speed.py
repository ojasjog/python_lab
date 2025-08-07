# You are using Python
N=int(input())
S=int(input())

bits=N*8/S


hours=bits//3600
minutes=(bits%3600)//60
seconds=bits%60

x=int(hours)
y=int(minutes)
z=int(seconds)
print(f"Download Time: {x} hours, {y} minutes, and {z} seconds")
