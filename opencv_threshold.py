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
    image = cv.imread('nuts.jpg',cv.IMREAD_GRAYSCALE)

    # Threshold
    # cv.threshold( src, thresh, maxval, type) -> retval, dst
    retval, process_image = cv.threshold(image, current_trackbar_value, 255, cv.THRESH_BINARY_INV)

    # Näitame pilti
    cv.imshow(window_name, process_image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()