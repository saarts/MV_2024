"""Operaatorid."""
import math


a = 5
b = 3

#Liitmine
print(a + b)

#Lahutamine
print(a - b)

#Korrutamine
print(a * b)

#Jagamine
print(a / b)

#Jagamine täisarvuks
print(a // b)

#Jäägiga jagamine
print(a % b)

#Astmesse võtmine
print(a ** b)
print(pow(a, b))

#Komakohad
division = a / b
print(division)
print(math.floor(division))
print(math.ceil(division))

#Suuremvõrdne
print(a >= b)

#Väiksem võrdne
print(a <= b)

#Mitte võrdne
print(a != b)

#Võrdne
print(a == b)

#Lihtsad võrdused
print(a < b)
print(a > b)

#Ruutjuur
print(math.sqrt(9))
print(9 ** (1/2))

"""Convert days, minutes, hours, seconds into minutes
Use input for asking values from the user

days = 0
hours = 1
minutes = 5
seconds = 0

output:
65
"""

days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

print((days * 1440) + (hours * 60) + minutes + (seconds // 60))
