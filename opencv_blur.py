import cv2 as cv

def on_change(value):
    pass


# Akna nime muutuja
window_name = 'Tore aken jah'

# Eelnimetame akna
cv.namedWindow(window_name)

# Loome juhtriba
# cv.createTrackbar(trackbarname, winname, value, count, TrackbarCallback, userdata = 0)
cv.createTrackbar('Threshold', window_name, 127, 255, on_change)

# Otsige pilt, mille puhul saaks threshold abil järgmise sammuga midagi tuvastada. 


# tsükkel algab
while True:
    # Loeme juhtriba väärtuse
    current_trackbar_value = cv.getTrackbarPos('Threshold', window_name)

    # Laeme pildi hallina
    image = cv.imread('nuts.jpg')

    #Gaussian blur // ksize - paaritud arvud
    #result_image = cv.GaussianBlur(image, (9, 9),9,0,9,cv.BORDER_REFLECT)
    
    #Median blur
    #result_image = cv.medianBlur(image, 9) 
    
    #Piirjooned
    result_image = cv.Canny(image, 255, 255)

    #Dilate - laiendab
    #result_image = cv.dilate(result_image, (5, 5), iterations=9)
    
    #Erode - kitsendab 
    #result_image = cv.erode(result_image, (1, 1), iterations=2)

    # Näitame pilti
    cv.imshow(window_name, result_image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()