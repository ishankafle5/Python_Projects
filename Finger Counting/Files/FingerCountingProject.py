import cv2
import time
import os
import HandTrackingModule as htm

wCam,hCam=1080,720
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
folderPath="Images"
mylist=os.listdir(folderPath)
print(mylist)
overlayList=[]
for imagePath in mylist:

    image=cv2.imread(f'{folderPath}/{imagePath}')
    print(f'{folderPath}/{imagePath}')
    overlayList.append(image)
print(len(overlayList))
pTime=0


detector=htm.handDetector(detectionCon=int(0.50))

tipid=[4,8,12,16,20]

while True:
    sucess,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        finger=[]
        for i in range(0,5):
            if lmList[tipid[i]][2] < lmList[tipid[i]-2][2]:

                finger.append(1)
            
            else:
                finger.append(0)
        
        print(finger)
        time.sleep(1)

        # if(lmList[8][2] < lmList[6][2]):
        #     print("Index finger is up")

        # if (lmList[8]  [2] < lmList[6][2]) and (lmList[12][2] < lmList[10][2]) and  (lmList[16][2] < lmList[14][2]):
        #     print("Index finger open")
            # break


    # print(lmList)
    h,w,c=overlayList[0].shape
    print(h,w,c)
    img[0:h,0:w]=overlayList[0]

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'{int(fps)}',(400,70),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,0),3)
    cv2.imshow("Image",img)
    if cv2.waitKey(10)==ord("a"):
        break


