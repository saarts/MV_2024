import cv2 as cv


def on_change(value):
    pass



# Laeme pildi hallina
image = cv.imread('nuts.jpg', cv.IMREAD_GRAYSCALE)

height,width = image.shape[:2]

image = cv.resize(image, (int(height/2), int(width/2)))


# Akna nime muutuja
window_name = 'Tore aken jah'

# Eelnimetame akna
cv.namedWindow(window_name)

# Loome juhtriba
# cv.createTrackbar(trackbarname, winname, value, count, TrackbarCallback, userdata = 0)
cv.createTrackbar('Threshold', window_name, 127, 255, on_change)


# tsükkel algab
while True:
    # Loeme juhtriba väärtuse
    current_trackbar_value = cv.getTrackbarPos('Threshold', window_name)

    # hägustame
    result_image = cv.medianBlur(image, 19)  
    
    # thresholding
    retval, result_image = cv.threshold(result_image, current_trackbar_value, 255, cv.THRESH_BINARY_INV)

    #leiame kontuurid
    contours, hirearchy = cv.findContours(result_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    number_of_filtered_contours = 0
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 25000:
            number_of_filtered_contours += 1
            x,y,w,h = cv.boundingRect(contour)
            cv.rectangle(result_image,(x,y),(x+w,y+h),(255,255,255))
    
    cv.putText(result_image, "Leitud", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.putText(result_image, str(len(contours)), (250, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.putText(result_image, "Filtreeritud", (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.putText(result_image, str(number_of_filtered_contours), (250, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


    # Näitame pilti
    cv.imshow(window_name, result_image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()