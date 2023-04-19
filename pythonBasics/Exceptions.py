# 2 items will be added to cart

ItemsInCart = 0

# if ItemsInCart !=2:
#    raise Exception("Products cart count not matching")

if ItemsInCart !=2:
    pass

assert(ItemsInCart == 0)

try:
    with open('test.txt', 'r') as reader:
        print(reader.read())

except:
    print("Some how I reached this block because there is failure in try block")

finally:
    print("Finally code of block would execute after passing the test")



try:
    with open('filelog.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("Finally code of block would execute after failing the test")
