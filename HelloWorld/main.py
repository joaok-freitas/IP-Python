def testfunc():
    print("Func 1")
    print("Func 2")
    print("Func 3")

def testfunc2():
    if age >=18:
        print("maior")
    else:
        print("menor")

print("first")
a = 30
b = 500.30
c = 0
c = c + a + b
if __name__ == '__main__':
    print("main")
    testfunc()

print("Type your name")
name = input()
if name != "":
    print("Hello " + name)
    age: int = input()
else:
    print("Hello world")
