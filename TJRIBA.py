import math

print("NOTICE!!!!!    THIS PROGRAM IS ONLY FOR 2ND EQUATION aX² +bX +c")
print("write ur equation :")
def discriminant(a,b,c):
    return b**2-4*a*c
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
Equation="aX²+bX+C"
D= discriminant(a,b,c)
print(discriminant(a, b, c))
s1=-b/(a*2)
s2=(-b-math.sqrt(D))/(a*2)
s3=(-b+math.sqrt(D))/(a*2)
if D<0 :
    print("this equation doesn't have a solution")
elif D==0:
    print("S=[",s1,"]")
elif D>0 :
    print("S=[",s2,"/",s3,"]")