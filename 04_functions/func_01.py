

def oblicz_promien(promien):
    pole = 3.14 * promien**2
    return pole

promien = int(input("Podaj promien: "))
print(" pole koła: ", oblicz_promien(promien))
