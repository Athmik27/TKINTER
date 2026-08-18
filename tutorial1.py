# closure example with parameters
def message_type(msg):
    message=msg
    def inner():
        print(msg)
    return inner
a=message_type("HI")
a()
b=message_type("Hello")
b()

# closure example without parameters
def outer():
    x=10
    def inner():
        print(x)
    return inner
f=outer()
f()