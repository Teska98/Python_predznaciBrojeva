n = int
p=0
r=0
while n!=0:
    n=int(input())
    if n>0:
        p=p+1
    elif n<0:
        r=r+1
if p>r:
   print("Ima vise pozitivnih brojeva")
if p<r:
   print("Ima vise negativnih brojeva")
if p==r:
   print("Isti je broj pozitivnih i negativnih brojeva")
