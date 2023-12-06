import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nuevaLista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)

print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(nuevaLista),
    random.choices(nuevaLista, k=2),
    random.choices("abcdefghijkl", k=2),
    "".join(random.choices("abcdefghijkl", k=2))
)

caracteres = string.ascii_letters
digitos = string.digits

seleccion = random.choices(caracteres + digitos, k=16)
print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)
