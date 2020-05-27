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
video_name='NV_42.mp4'
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
j=0
final_fps=4
block=1
selected_frames=[]
while (len(selected_frames)<final_fps):
    r=randint(1,fps)
    if r not in selected_frames:
        selected_frames.append(r)
selected_frames.sort()

def update_frames(lb,ub):
    selected_frames=[]
    while (len(selected_frames) < final_fps):
        r = randint(lb, ub)
        if r not in selected_frames:
            selected_frames.append(r)
    selected_frames.sort()
    return selected_frames

v_name=video_name.split('.')
v=v_name[0]

with open('training.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['Name','R-Sho','L-Sho','L-Elb','R-Elb','L-Wr','R-Wr','L-Hip','R-Hip','L-Knee','R-Knee','L-Ank','R-Ank','Color','Class'])
    while (cap.isOpened()):
        if j == final_fps:
            lb = fps * block
            ub = fps * (block + 1)
            selected_frames = update_frames(lb, ub)
            j = 0
            block += 1
        ret, frame = cap.read()
        if ret == False:
            if i<frame_count:
                print("Broken frame identified and ignored")
                continue
            else:
                break
        fname = v + '-frame' + str(i) + '.jpg'
        if i in selected_frames:
            #cv2.imwrite('extracted_frames/' + fname, frame)
            j += 1
            apply_yolo(fname, frame,writer)
            print(j, selected_frames)
        i += 1

cap.release()
cv2.destroyAllWindows()