import cv2
import numpy as np
import argparse
import os
import csv
import time
from random import randint
import subprocess
p = subprocess.call('cd .. ', shell=True)
protoFile = "C:/Users/Bipin Gowda/PycharmProjects/GodsEye/multipose_model/pose_deploy_linevec.prototxt"
weightsFile = "C:/Users/Bipin Gowda/PycharmProjects/GodsEye/multipose_model/pose_iter_440000.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
environment={
    'ATM':'model_jairaj_home',
    'Sports':'sports',
}
#Apply yolo to the selected frames
def apply_yolo(fname,frame,count,total_count,env):
    from multipose_test import apply_pose_estimate
    start1=time.time()
    count,tt=apply_pose_estimate(frame, net, fname, count, environment[env])
    total_count=total_count+tt
    end1=time.time()
    print('Time taken:',(end1-start1))
    return count,total_count

def update_frames(lb,ub,ffps):
    selected_frames=[]
    while (len(selected_frames) < ffps):
        r = randint(lb, ub)
        if r not in selected_frames:
            selected_frames.append(r)
    selected_frames.sort()
    return selected_frames

def alpha(name,f,env):
    count=0
    total_count=0
    # Opens the Video file
    video_name = name
    cap = cv2.VideoCapture('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/videos/' + video_name)

    # Find FPS
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = int(cap.get(cv2.cv.CV_CAP_PROP_FPS))
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    i = 0
    j = 0
    final_fps = f
    block = 1
    n=1
    selected_frames = []
    while (len(selected_frames) < final_fps):
        r = randint(1, fps)
        if r not in selected_frames:
            selected_frames.append(r)
    selected_frames.sort()

    v_name = video_name.split('.')
    v = v_name[0]

    while (cap.isOpened()):
        if j == final_fps:
            lb = fps * block
            ub = fps * (block + 1)
            selected_frames = update_frames(lb, ub, final_fps)
            j = 0
            block += 1
        ret, frame = cap.read()
        if ret == False:
            if i < frame_count:
                print("Broken frame identified and ignored")
                continue
            else:
                break

        if i in selected_frames:
            fname = v + '-frame_'+str(f)+'_'+ str(n) + '.jpg'
            #cv2.imwrite('extracted_frames/' + fname, frame)
            j += 1
            n += 1
            count,total_count=apply_yolo(fname, frame,count,total_count,env)
            print(j, selected_frames)
        i += 1

    cap.release()
    cv2.destroyAllWindows()
    import sys
    sys.path.insert(0, 'C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output')
    from output.generate_video import generate
    generate(v,f)
    return fps,int(round(total_count/count))