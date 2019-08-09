#!/usr/bin/env python
# coding: utf-8

hemiList = ["rh","lh"]

fsSubjName = ["ab_data","bg_data","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]
surfSubjName = ["ab","bg","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]

#extract data from localizer blur epi data
import os
import numpy as np
import subprocess
def listdir(path,hemi):
    num = []
    for file in os.listdir(path):
        temp = file.split(".")
        if temp[0] == "newNodes_"+hemi+"_SurfCoord":
            num.append(temp[1])
#             print temp,temp[1]
    return num

run = range(1,3)
for s in range(0,len(fsSubjName)):
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName[s]+"/SUMA"
    blurFilePath = "/mnt/data_disk/projects/all_subj/surfaceProj/afni/localizerExp/surfAnalysis/"+surfSubjName[s]+"/"+surfSubjName[s]+".surf.results"

    for hemi in hemiList:
        num = listdir(filePath,hemi)
        for r in run:
            for i in range(len(num)):
                command1 = "cd "+filePath+";
                ConvertDset -input "+blurFilePath+"/pb04."+surfSubjName[s]+".surf."+hemi+".r0"+str(r)+".blur.niml.dset                 
                -node_select_1D newNodes_"+hemi+"_SurfCoord."+num[i]+".1D                 
                -o_1D_stdout > "+hemi+"_roi"+num[i]+".run"+str(r)+".Nodesvals.txt"

                subprocess.call(command1, shell=True)
