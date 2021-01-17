import cv2, time
from datetime import datetime
import argparse
import os




face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
first_frame=None
t=0
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    if frame is not None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
        for x,y,w,h in faces:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            todays_date =datetime.now().strftime('%Y-%b-%d-%H-%M-%S-%f')
            cv2.imwrite("pic_resize"+str(todays_date)+".jpg",img)
            #print(img)
            #t=t+1
        cv2.imshow("gottcha",frame)
        key=cv2.waitKey(1)

        if key==ord('q'):
            ap = argparse.ArgumentParser()
            ap.add_argument("-ext", "--extension", required=False, default='jpg', help="extension name. default is 'jpg'.")
            ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
            args = vars(ap.parse_args())

            # Arguments
            dir_path = '.'
            ext = args['extension']
            output = args['output']

            images = []
            for f in os.listdir(dir_path):
                if f.endswith(ext):
                    images.append(f)

            # Determine the width and height from the first image
            image_path = os.path.join(dir_path, images[0])
            frame = cv2.imread(image_path)
            cv2.imshow('video',frame)
            height, width, channels = frame.shape

            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
            out = cv2.VideoWriter(output, fourcc, 5.0, (width, height))

            for image in images:

                image_path = os.path.join(dir_path, image)
                frame = cv2.imread(image_path)

                out.write(frame) # Write out frame to video

                cv2.imshow('video',frame)
            break
video.release()
cv2.destroyAllWindows()
