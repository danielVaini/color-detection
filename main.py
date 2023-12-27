import cv2
from utils import get_color

# Add the colors you want to detect
yellow = [0, 255, 255] # BGR colorspace
red = [0, 0, 255] # BGR colorspace

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    bbox_yellow = get_color(frame, yellow)
    bbox_red = get_color(frame, red)
    
    # Draw a rectangle
    if bbox_yellow is not None:
        x1, y1, x2, y2 = bbox_yellow  
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 5)
        org = [x1, y1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 255, 0)
        thickness = 2

        cv2.putText(frame, 'Yellow', org, font, fontScale, color, thickness)
        
        
    if bbox_red is not None:
        x1, y1, x2, y2 = bbox_red  
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
        org = [x1, y1]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2

        cv2.putText(frame, 'Red', org, font, fontScale, color, thickness)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()