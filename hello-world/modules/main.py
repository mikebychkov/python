
print(__name__)

import utility as u
from shopping import cart 
import shopping.vendors.amazon as amz


def main():
    print("Hello from main file!")

    print(u.m_sum(1,3,5))

    cart.addToCart([1,2])
    cart.listCart()

    amz.listGoods()


if __name__ == "__main__":
    main()
