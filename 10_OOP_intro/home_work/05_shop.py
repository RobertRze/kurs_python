class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print('Dodano', product)

    def zobacz_produkt(self):
        pass
        # Wyświetl w ładny sposób info o dostępnych produktach

    def przymierz_produkt(self):
        pass
        #Jeśli produkt o podanej nazwie istnieje w liście produktów:
        #    Wyświetl informację o możliwości przymierzenia produktu
        #W przeciwnym razie:
        #    Wyświetl informację o niedostępności produktu

    def kup_produkt(self):
       pass
       #Jeśli produkt o podanej nazwie istnieje w liście produktów:
       #     Wyświetl informację o zakupie produktu
       #     Usuń produkt z listy produktów
       # W przeciwnym razie:
       #     Wyświetl informację o niedostępności produktu

    def zwroc_produkt(self):
       pass
       # Jeśli produkt posiada nazwę i cenę
       #Wyświetl informację o możliwości zwrotu produktu
       #     Dodaj produkt ponownie do listy produktów
       # W przeciwnym razie:
        #    Wyświetl informację o braku możliwości zwrotu produktu

# spodnie = Product('spodnie', 1.11)
# bluza = Product('bluza', 3.22)
# buty = Product('buty', 10)


Shop.add_product(Product('spodnie', 1))




