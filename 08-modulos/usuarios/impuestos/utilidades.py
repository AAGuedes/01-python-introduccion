"Clase utilidades"

if __name__ != "__main__":
    # from ..gestion.crud import guardar # Import relativo
    from usuarios.gestion.crud import guardar # Import absoluto

    print("utilidades.py", __name__)

    def pagar_impuestos():
        "Función pagar impuestos"
        print("Pagando impuestos")
        guardar()

if __name__ == "__main__":
    print("Tarea de mantenimiento")
