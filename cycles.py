"""For loop."""

example_text = "Caterpillar"
test_condition = "cATerP"

print(test_condition.lower() in example_text.lower())

for i in range(10):
    print(i)
    
print("..............")
    
for i in range(4,9):
    print(i)

print("..............")

for i in range(4, 9, 3):
    print(i)

#range(lõpp)
#range(alg, lõpp)
#range(alg, lõpp, samm)

print("..............")

juurikad = ["kaalikas", "kartul", "porgand", "rõigas", "maasikas", "sibul"]

for juurikas in juurikad:
    print(juurikas)

puuvili = "kirss"

for letter in puuvili:
    print(letter)
    
omadused = ["punane", "maitsev", "suur"]
toidud = ["õun", "tomat", "tort"]

for omadus in omadused:
    for toit in toidud:
        print(omadus, toit)
        
test_text = "Mõistlik lause, mida võiks kasutada"
print(len(test_text))
print(test_text[:4])
print(test_text[2:8])
print(test_text[2:30:3])
print(test_text[::-1])
print(test_text[5:-5])



"""Arvuta kokku paaritud arvud, kui sisestada number

Näiteks:

7
1 + 3 + 5 + 7 = 16

"""

test_arv = input("Sisesta number: ")

total = 0

for num in range(int(test_arv) + 1):
    if num % 2 == 1:
        total += num

print(total)

#While tsükkel
i = 0
while i < 10:
    i += 1
    print(i)
    
