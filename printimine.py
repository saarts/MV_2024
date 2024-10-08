"""
Tere, mis su nimi on: Albert
Tere, Albert, kui vana sa oled?: 75
Oled Albert ja sa oled 75
"""
name = input("Tere, mis su nimi on: ")

#Näide, kuidas print lõpeb end-iga
print("Tere, " + name +", kui vana sa oled: ",end="")
age = input()

#Erinevad viisid, kuidas printida
print("Oled " + name + " ja sa oled " + age)
print("Oled", name, "ja sa oled", age)
print(f"Oled {name} ja sa oled {age}")
