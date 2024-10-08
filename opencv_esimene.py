# Võtame opencv kasutusele
import cv2  

# Open cv versiooni kontroll
print(cv2.__version__)

# Avame/loeme pildi
image = cv2.imread('testpic.png')

#Kontrollime, kas pilt on olemas
if image is None:
    print("Error opening image")
    exit()

# Kuvame pildi aknas, millele anname nime
cv2.imshow('Akna nimi on see argument', image)

# Ootame klahvi vajutust - 0-st erinev on timeout väärtus
cv2.waitKey(0)

# Pildi salvestamine
cv2.imwrite('new_pic.png', image)