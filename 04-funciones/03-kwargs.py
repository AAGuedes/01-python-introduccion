"""
Kwargs
"""


def get_product(**datos):
    """
    Imprime todos los Keyword Arguments recibidos
    """
    print(datos) # El formato corresponde con un diccionario
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iPhone",
            desc="Un iPhone 1")
