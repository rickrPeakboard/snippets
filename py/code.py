def hello():
    print("hello world")

def demo(parameter):
    if parameter:
        print("one")
    else:
        print("two")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)

hello()
demo(True)
demo(0)
demo(False)
factorial(10)