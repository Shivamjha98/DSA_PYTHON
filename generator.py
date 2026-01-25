# send and close

# send() - whatever we want to yield -- we can send it
# close() - close generator

def gen_func():
    while True:
        receive = yield
        print("received:", receive)

it_obj=gen_func()

print(next(it_obj))

it_obj.send("hello")
it_obj.send("world")
