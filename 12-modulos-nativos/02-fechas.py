import time
from datetime import datetime

print(time.time())

fecha = datetime(2023, 1, 1)
print(fecha)

ahora = datetime.now()
print(ahora)

# Más info sobre directivas: https://docs.python.org/3/library/datetime.html
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

print(fecha.strftime("%Y\%m\%d"))

print(fecha > ahora)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
