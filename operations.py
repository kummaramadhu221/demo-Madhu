print("arithmetic operators")
a=7
b=2
print(f"a={a},b={b}")
print("sum:a+b",a+b)
print("sub:a-b",a-b)
print("mul:a*b",a*b)
print("div:a/b",a/b)
print("floor division:a//b",a//b)
print("modulo:a%b",a%b)
print("power:a power b",a**b)


print("comparision operations")
a=5
b=2
print(f"a={a},b={b}")
print("a==b=",a==b)
print("a!=b=",a!=b)
print("a>b=",a>b)
print("a<b=",a<b)
print("a>=b=",a>=b)
print("a<=b=",a<=b)



print("assignment operations")
a=10
b=5
print(f"a={a},b={b}")
a+=b        #a=a+b
print("a+=b is ",a)




print("logical operations")
print("logical AND")
print(True and True)
print(True and False)
print("logical OR")
print(True or False)
print("logical NOT")
print(not True)



print("bitwise operations")
a=10
b=4
print(f"a{a},b={b}")
print("a&b=",a&b)
print("a|b=",a|b)
print("~a=",~a)
print("a^b=",a^b)




print("membership operators")
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)



print("identity operators")
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(f"x1={x1},y1={y1},x2={x2},y2={y2},x3={x3},y3={y3}")
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
