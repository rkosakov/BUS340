class Product:
    def __init__(self, name = "", price = 1):
        self._name = name
        self._price = price

    def getName(self):
        return self._price

    def getPrice(self):
        return self._price

    def setName(self, name):
        self._name = name

    def setPrice(self, price):
        self._price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        elif self._name == other.__name:
            return True

        return False


class TaxedProduct(Product):

    def __init__(self, tax = 0):
        super().__init__()
        self.__tax = tax

    def getTax(self):
        return self.__tax

    def setTax(self, tax):
        self.__tax = tax

    def getTotalPrice(self):
        return super()._price + (super()._price * self.__tax)

    def __str__(self):
        return f'Product Name: {super()._name} with a final price {self.getTotalPrice()}'



