import cv2
import numpy as np
import argparse
import os
import csv
import time
from random import randint

protoFile = "multipose_model/pose_deploy_linevec.prototxt"
weightsFile = "multipose_model/pose_iter_440000.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

#Apply yolo to the selected frames
def apply_yolo(fname,frame,writer):
    from multipose import apply_pose_estimate
    start=time.time()
    apply_pose_estimate(frame, net, fname,writer)
    end=time.time()
    print('Time taken:',(end-start))

# Opens the Video file
video_name='J_NV1.mp4'
cap = cv2.VideoCapture('videos/'+video_name)

#Find FPS
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver) < 3:
    fps = int(cap.get(cv2.cv.CV_CAP_PROP_FPS))
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else:
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_count)
i=0
v_name=video_name.split('.')
v=v_name[0]

with open('training_all.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['Name','R-Sho','L-Sho','L-Elb','R-Elb','L-Wr','R-Wr','L-Hip','R-Hip','L-Knee','R-Knee','L-Ank','R-Ank','Color','Class'])
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            if i<frame_count:
                print("Broken frame identified and ignored")
                continue
            else:
                break
        fname = v + '-frame' + str(i) + '.jpg'
        apply_yolo(fname, frame,writer)
        i += 1
cap.release()
cv2.destroyAllWindows()