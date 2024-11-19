import cv2 as cv
import numpy as np

def on_change(value):
    pass

# Akna nime muutuja
window_name = 'Tore aken jah'

# Eelnimetame akna
cv.namedWindow(window_name)

# Loome juhtriba
# cv.createTrackbar(trackbarname, winname, value, count, TrackbarCallback, userdata = 0)
cv.createTrackbar('Threshold', window_name, 220, 255, on_change)

# Otsige pilt, mille puhul saaks threshold abil järgmise sammuga midagi tuvastada. 


# tsükkel algab
while True:
    # Loeme juhtriba väärtuse
    current_trackbar_value = cv.getTrackbarPos('Threshold', window_name)
    
    # Laeme pildi hallina
    image = cv.imread('balls.jpg',cv.IMREAD_GRAYSCALE)

    # Threshold
    # cv.threshold( src, thresh, maxval, type) -> retval, dst
    retval, process_image = cv.threshold(image, current_trackbar_value, 255, cv.THRESH_BINARY)

    params = cv.SimpleBlobDetector_Params()

    params.minArea = 10000
    params.maxArea = 1000000

    detector = cv.SimpleBlobDetector_create(params)
    key_points = detector.detect(process_image)
    

    process_image = cv.drawKeypoints(process_image, key_points, np.array([]), (0, 255, 0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.putText(process_image, str(len(key_points)), (50, 300), cv.FONT_ITALIC, 1, (0, 0, 0), 2)

    # Näitame pilti
    cv.imshow(window_name, process_image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()