# Võtame opencv kasutusele
import cv2  

# Avame/loeme pildi
image = cv2.imread('testpic.png')

# Kontrollime, kas pilt on olemas
if image is None:
    print("Error opening image")
    exit()

# Suuruse muutmine
resized_image = cv2.resize(image,(500, 500))

# Mustvalge
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)

# Pildi suurus
im_height = gray_image.shape[0]
im_width = gray_image.shape[1]
# Pildi keskpunkt
center = (im_width/2, im_height/2)
# Pildi keeramismaatriks
rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1)
# Pildi keeramine
rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (im_width,im_height))

# Kuvame pildi aknas, millele anname nime
cv2.imshow('Akna nimi on see argument', rotated_image)
cv2.imshow('Akna', gray_image)

# Ootame klahvi vajutust - 0-st erinev on timeout väärtus
cv2.waitKey(0)


# Kõikide akende sulgemine
cv2.destroyAllWindows()