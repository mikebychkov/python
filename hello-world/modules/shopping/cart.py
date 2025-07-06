
print(__name__)

goods_cart = []

def addToCart(*goods):
    global goods_cart
    goods_cart = list(goods)

def listCart():
    global goods_cart
    print(goods_cart)
