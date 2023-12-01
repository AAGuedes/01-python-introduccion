"""
Métodos de strings
"""

ANIMAL = "   ardiLLa voladora "

print(ANIMAL.upper())
print(ANIMAL.lower())
print(ANIMAL.strip().capitalize())
print(ANIMAL.title())
print(ANIMAL.strip())
print(ANIMAL.lstrip())
print(ANIMAL.rstrip())
print(ANIMAL.find("LL"))
print(ANIMAL.replace("LL", "ll"))
print("LL" in ANIMAL)
print("LL" not in ANIMAL)
