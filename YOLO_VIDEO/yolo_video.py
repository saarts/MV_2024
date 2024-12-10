from ultralytics import YOLO
import cv2 as cv
import torch

torch.cuda.is_available()

#Laeme mudeli
model = YOLO('yolo11n.pt')

# Video laadimine # Webcam   cv.VideoCapture(0)
capture = cv.VideoCapture("videoplayback.mp4")

#Kontrollime, kas on võimalik avada
if not capture.isOpened():
    print("something exploded")
    exit()

while(True):
    
    #pilt võetud results-ist
    ret, image = capture.read()
    
    if not ret:
        print("Frame return error")
        break
        
    results = model(image)
    results = results[0]
    
    #Kastide ja tekstide joonistamine
    for box in results.boxes:
        coordinates = box.xyxy[0].tolist()
        confidence = round(box.conf[0].item(), 2)
        class_id = results.names[int(box.cls)]
        
        cv.rectangle(image,(int(coordinates[0]),int(coordinates[1])),(int(coordinates[2]),int(coordinates[3])),(255,0,0),2)
        cv.putText(image,class_id,(int(coordinates[0]),int(coordinates[1])),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv.putText(image,str(confidence),(int(coordinates[2]),int(coordinates[3])),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    
    cv.imshow('window', image)

    # Ootame nupu vajutust, et lõpetada tsükkel
    key = cv.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()