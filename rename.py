# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 22:28:26 2020

@author: user
"""
import os

root = "D:/omsa"
os.chdir(root)
subfolder = root+"/IAM_IYSE_videos/"

fileName = "Intro_to_analytics_playlist.csv"

with open(fileName) as f:
  lineList = f.readlines()

newList = [i.strip() for i in lineList]
newList.pop(0)

newFileName = ""

for i in range(0,len(newList)-2):
    
    path = subfolder + newList[i]
    
    for file in os.listdir(path):
        print (file)
        newFileName = file.replace(newList[i], "video_"+str(i+1))
        oldFile = path + "/" + file
        newFile = path + "/" + newFileName
        print (oldFile)
        print (newFile)
        os.rename(oldFile, newFile)

    oldPath = subfolder + newList[i]                      
    newPath = subfolder + "video_" + str(i+1)
    os.rename(oldPath, newPath)