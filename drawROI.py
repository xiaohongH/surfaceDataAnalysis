#!/usr/bin/env python
# coding: utf-8

# In[1]:


hemiList = ["lh","rh"]
subjname = "mm"
surfName = "mm"

filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+subjname+"/SUMA"


# In[2]:


#在surface上画ROI
#将1D文件转成dset文件
import subprocess

for hemi in hemiList:

    command = "cd "+filePath+";    ROIgrow -overwrite -spec "+subjname+"_"+hemi+".spec -surf_A "+hemi+".full.flat.patch.3d     -roi_nodes nodelocations_"+hemi+".1D -roi_labels PER_NODE -lim 1 -prefix "+hemi+"_SurfCoord"
    print command
    subprocess.call(command, shell=True)

    command2 = "cd "+filePath+";    ROIgrow -overwrite -spec "+subjname+"_"+hemi+".spec -surf_A "+hemi+".full.flat.patch.3d     -roi_nodes nodelocations_"+hemi+".1D -lim 1 -prefix "+hemi+"_SurfCoord_all"

    command3 = "cd "+filePath+";    ConvertDset -o_1D -add_node_index -input "+hemi+"_SurfCoord_all.1D -prefix SurfCoordRoi_"+hemi+"_all"

    subprocess.call(command2, shell=True)
    print command2

    subprocess.call(command3, shell=True)
    print command3


# In[3]:


#将有val的nodes index的文件，转成没有val的文件
import os
import numpy as np
def listdir(path,hemi):
    num = []
    for file in os.listdir(path):
        temp = file.split(".")
        if temp[0] == hemi+"_SurfCoord":
            num.append(temp[1])
    return num

def writeNewNodes(boldInfileDir,roiName):
    temp = []
    x =[]
    boldFinalDir = os.path.join(boldInfileDir,roiName)
    with open(boldFinalDir) as f:
        for line ,i in enumerate(f.readlines()):
            if i[0] != "#":
                temp.append(i.split("  ")[0])
        temp= np.array(map(int,temp))
        
    newfileName = os.path.join(boldInfileDir,"newNodes_"+roiName)
    f=open(newfileName,"w") 
    for i in range(len(temp)):
        f.write(str(temp[i])+"\n")
    f.close
    return temp


for hemi in hemiList:
    filePath = "/home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/"+subjname+"/SUMA"
    num = listdir(filePath,hemi)
    for i in range(len(num)):
        filename = hemi+"_SurfCoord."+num[i]+".1D"
        writeNewNodes(filePath,filename)


# In[1]:


#将每个小的roi的1D文件转成dset文件
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

hemiList = ["lh","rh"]
subjname = "ab_data"
surfName = "ab"

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


# In[ ]:




