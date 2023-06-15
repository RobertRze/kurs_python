# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
# Utwórz funkcję zwracającą tekst
# Utwórz dekorator przyjujący tę funkcję
# Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(func):
    def new_text():
        return func().upper()
    return new_text


@uppercase_decorator
def return_text():
    return 'text'


result = return_text()
print(result)
