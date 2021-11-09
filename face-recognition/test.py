
# import the opencv library
import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
array = []

cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()