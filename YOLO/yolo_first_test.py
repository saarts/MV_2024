
from ultralytics import YOLO
import cv2 as cv

#Laeme mudeli
model = YOLO('yolo11n.pt')

#Mudeli info
model.info()

#Söödame pildi mudelile ja saame tulemused
results = model('baltijaam.jpg')

print(results)

results = results[0]

for box in results.boxes:
    print("---------------------------------")
    print("Object class ", results.names[int(box.cls)])
    print("Coordinates: ", box.xyxy[0].tolist())
    print("Object confidence: ", box.conf[0].item())

while(True):
    
    #pilt võetud results-ist
    image = results.orig_img
    
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
