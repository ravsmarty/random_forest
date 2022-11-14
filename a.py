#use of if statements

a=5
b=6

if b > a:
    print(" a is greater than b")

m=6
n=6
if m>n:
    print("m is not equal")

elif m==n:
    print("m is equal to n")

x=77
y=66
if x>y:
    print("x is greater than y")

elif x==y:
    print("x is equal to y")

else:
    print("x is less than y")

#short hand if: if we have only one statements
if x>y: print("x is greater than y")

#and keywords
if x>y and x<y:
    print("this is true")
else:
    print(" it is false")

if x>y or x<y:
    print("this is true")
else:
    print("this is false")

#nested if: if there is if in under if
z=5
if z>43:
    print("above 20")
    if z>20:
        print("and also above 20")
    else:
        print("not 20")

#pass statements: if statements are empty then we use this
d=44
e=66

if d>e:
    
    pass


