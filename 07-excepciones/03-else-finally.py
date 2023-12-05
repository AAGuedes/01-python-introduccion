"""
Bloques else y finally
"""

try:
    number1 = int(input("Input first number: "))
except Exception as e:
    print("An error happened!")
else:
    print("No error happened!")
finally:
    print("Input finished!")
