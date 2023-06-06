

class Shop:
    def __init__(self):
        self.products = [('spodnie', 39), ('buty',100), ('koszula', 10)]



    def add_product(self, product):
        self.products.append(product)
        print('Dodano')


    def show(self):
        for item, price in self.products:
            print(item, 'cena: ', price, 'PLN')


    def show_product(self, name):
        # for item, price in self.products:
        #     if item == nema:
        #         print(item, 'cena: ', price, 'PLN')
        #         break
        prods = dict(self.products)
        if name not in prods.keys():
            print('nie ma')
        else:
            print(name, '->', prods[name])


    def try_product(self, name):
        prods = dict(self.products)
        if name not in prods.keys():
            print('nie ma')
        else:
            print('Przymierzam', name)

    def buy_product(self, name):
        found = False
        for item, price in self.products:
            if name == item:
                found = True
                product = (item, price)
                print('Kupuję', product)
                self.products.remove(product)
                break
        if not found:
            print('Brak produktu do kupieniaa')

    def return_product(self, name, price):
        prods = dict(self.products)
        if name not in prods.keys():
            product = (name, price)
            self.products.append(product)
            print('Zwrócono')
        else:
            print('produkt z innego sklepu', name)


def main():
    myshop = Shop()
    myshop.show()
    myshop.show_product('buty')
    myshop.show_product('lal')
    myshop.try_product('buty')
    myshop.try_product('lal')
    myshop.buy_product('boty')
    myshop.buy_product('buty')
    myshop.show()
    myshop.return_product('buty', 100)
    myshop.show()
    myshop.return_product('buty', 1)
    myshop.show()


if __name__ == '__main__':
    main()
