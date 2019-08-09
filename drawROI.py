#!/usr/bin/env python
# coding: utf-8

hemiList = ["lh","rh"]
fsSubjName = ["ab_data","bg_data","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]
surfSubjName = ["ab","bg","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]

filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+subjname+"/SUMA"


#convert each .1D file to .dset
import os
import subprocess

def listdir(path,hemi):
    num = []
    for file in os.listdir(path):
        temp = file.split(".")
        if temp[0] == "newNodes_"+hemi+"_SurfCoord":
            
            num.append(temp[1])
    print num
    return num

for hemi in hemiList:
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+subjname+"/SUMA"
    print filePath
    
    num = listdir(filePath,hemi)
    for i in range(len(num)):
        command = "cd "+filePath+";        ConvertDset -o_1D -add_node_index -input newNodes_"+hemi+"_SurfCoord."+num[i]+".1D -prefix SurfCoordRoi."+hemi+"_"+num[i]
        
        print command
        subprocess.call(command, shell=True)

#ConvertDset -o_1D -add_node_index -input lh_SurfCoord_all.1D -prefix SurfCoordRoi_lh_all
# ConvertDset -o_1D -add_node_index -input allnodelocations_rh.1D  -prefix SurfCoordRoi_rh_all


