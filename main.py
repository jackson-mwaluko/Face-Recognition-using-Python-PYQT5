import sys
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import MyIcon_rc


class FaceDetection(QMainWindow):
    def __init__(self):
        super(FaceDetection,self).__init__()
        loadUi('Interface.ui',self)
        self.image=None
        self.processedImage=None
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.toggled.connect(self.start_Video)
        self.video_Enabled=False

        self.pushButton_10.setCheckable(True)
        self.pushButton_10.toggled.connect(self.detect_webcam_face)
        self.face_Enabled=False
        self.faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

      

    def detect_webcam_face(self,status):
            if status:
                self.pushButton_10.setText('Stop Detection')
                self.face_Enabled=True
            else:
                self.pushButton_10.setText('Detect Face')
                self.face_Enabled=False

    def start_Video(self,status):
            if status:
                self.pushButton_11.setText('Stop Video')
                self.video_Enabled=True
                self.start_webcam(self)
            else:
                self.pushButton_11.setText('Take Video')
                self.video_Enabled=False   
                self.start_webcam(self)         

    def start_webcam(self,condition):
        if(condition.video_Enabled): 
           self.capture=cv2.VideoCapture(0)
           self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,200)
           self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 100)

           self.timer=QTimer(self)
           self.timer.timeout.connect(self.update_frame)
           self.timer.start(5)
        else:
             self.timer.stop()  

    def update_frame(self):
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)

        self.displayImage(self.image, 1)
        if(self.face_Enabled):
            detected_image=self.detect_face(self.image)
            self.displayImage(detected_image,1)
        else:
            self.displayImage(self.image,1)


    def detect_face(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.faceCascade.detectMultiScale(gray,1.2,5,minSize=(90,90))

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

        return img

    def stop_webcam(self):
        self.timer.stop()


    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB
        outImage=outImage.rgbSwapped()

        if window==1:
            self.label_3.setPixmap(QPixmap.fromImage(outImage))
            self.label_3.setScaledContents(True)

        if window==2:
            self.label_3.setPixmap(QPixmap.fromImage(outImage))
            self.label_3.setScaledContents(True)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=FaceDetection()
    window.show()
    sys.exit(app.exec_())