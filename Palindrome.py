n=121
temp=n
r=0
pal=0
while n>0:
    r=n%10
    pal=pal*10+r
    n=n/10

if r==temp:
    print ("This is palindrome.")
else:
    print ("Not palindrome.")
