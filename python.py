import this

import turtle

# turtle.pensize(4)
# turtle.pencolor('red')

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# turtle.mainloop()
# print("hello")

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>12
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

def gcd(x = 0,y = 0):
    """sdfasdf"""
    (x,y) = (y,x) if x >y else (x,y)
    print (x,y)
    for num in range(x,1,-1):
        if x % num == 0 and y % num == 0:
            return num

def lcm(x,y):
    return x * y // gcd(x,y)

if __name__ == "__main__":
    a = int(input('请输入一个数字:'))
    b = int(input('请输入另一个数字:'))
    print(gcd(a,b))
    print(lcm(a,b))