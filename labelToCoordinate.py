#!/usr/bin/env python
# coding: utf-8

# In[11]:

hemi = ["rh","lh"]
fsSubjName = ["ab_data","bg_data","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]
surfSubjName = ["ab","bg","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]

# In[5]:

#mri_annotation2label: to convert an annotation file into multiple label files or into a segmentation 'volume'.
#convert the lh/rh.aparc.annot to alot of label, each label is a brain area: Frontal lobe, parietal lobe, occipital lobe etc.

import subprocess

for s in range(0,len(fsSubjName)):
    inFileName = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer"
    outFileName = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName[s]+"/SUMA/"

    for h in hemi:
        command1 = "mkdir "+outFileName+h+"\\"
        print command1
        subprocess.call(command1,shell = True)
        
        command = "bash;mri_annotation2label --subject "+fsSubjName[s]+" --hemi "+h+" --annotation  aparc.a2009s --outdir "+outFileName+h
        subprocess.call(command,shell = True)

# In[7]:
#combine several labels(.G_oc-temp_med-Parahip.label,.G_oc-temp_lat-fusifor.label,S_oc-temp_med&Lingual.label...) into a single mask;

import os
import numpy as np
import subprocess

def writeNewLabel(infileDir,newfileName):
    temp = []
    x =[]
    with open(infileDir) as f:
        for line ,i in enumerate(f.readlines()):
            if line > 1:
                temp.append(i.split("  ")[0])
        temp= np.array(map(int,temp))
            
    f=open(newfileName,"a")
    for i in range(len(temp)):
        f.write(str(temp[i])+"\n")
    f.close
    return temp

hemi = ["lh","rh"]

labelName = [".G_oc-temp_med-Parahip.label",".S_oc-temp_med&Lingual.label",
             ".G_oc-temp_lat-fusifor.label",".S_oc-temp_lat.label",".G_oc-temp_med-Lingual.label",
             ".S_collat_transv_ant.label"]

for s in range(0,len(fsSubjName)):
    addLabelName = "+Parahip+Lingual+fusifor.1D"
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName[s]+"/SUMA"

    for h in range(len(hemi)):
        for i in labelName:
            finalLabelName = hemi[h] + i

            newFinalLabelName = os.path.join(filePath,hemi[h]+addLabelName) 
            finalFileName = os.path.join(filePath,hemi[h],finalLabelName)
            print finalFileName
            #以追加的方式把多个label中的vertex，写入新的文件中
            print newFinalLabelName
            writeNewLabel(finalFileName,newFinalLabelName)


# In[8]:
#convert the above .label file to .dset file, so that python can read the file and get all the nodes of this big mask.

hemi = ["lh","rh"]

addLabelName = "+Parahip+Lingual+fusifor"

for s in range(0,len(fsSubjName)):
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName[s]+"/SUMA"
    #将label中的vertex转化成dset文件
    for h in range(len(hemi)):
        inLabelName = os.path.join(filePath,hemi[h]+addLabelName+".1D") 
        print inLabelName
        outputFile = os.path.join(filePath,hemi[h]+addLabelName)
        #将1D文件转成dset文件
        command = "cd "+filePath+";        ConvertDset -o_1D -add_node_index -input "+inLabelName+" -prefix "+outputFile
        print command
        subprocess.call(command, shell=True)


# In[9]:

#the t-test statistic results of EIP localizer data preprocessing,(eg:ab subject and lh hemisphere): stats.ab.surf.lh.niml.dset
#convert the t-test statistic results(eg,stats.ab.surf.lh.niml.dset) to .1D.dset,
#so that python can read nodes and the corespond t value. 

import os
import subprocess
hemi = ["lh","rh"]
for s in range(0,len(fsSubjName)):
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/afni/localizerExp/surfAnalysis/"+surfSubjName[s]+"/"+surfSubjName[s]+".surf.results/"
    for h in hemi:
        command = "cd "+filePath+"; ConvertDset -o_1D -input "+filePath+"/stats."+surfSubjName[s]+".surf."+h+".niml.dset"+" -prefix stats."+surfSubjName[s]+"."+h
        print command
        subprocess.call(command, shell=True)
        
# In[12]:
#compute the maximum and minimum t value of the statistic dataset in the above mask.
#extrat the correspond vertex,
#so that can use this two vertex to draw a line.
#vertex num starts from 0
import pandas as pd
import numpy as np
def readStatsData(infileDir):
    temp = []
    with open(infileDir) as f:
        for line ,i in enumerate(f.readlines()):
            if i[0] == "#" and line > 5:
                break
            if i[0] != "#":
                temp.append(i.split(" ")[9])
    return temp

def readRoiNodes(infileDir):
    temp = []
    with open(infileDir) as f:
        for line ,i in enumerate(f.readlines()):
            temp.append(i.split("\n")[0])
    return temp

def getMaxMinNodes(hemi,fsSubjName,surfSubjName):
    infileDir = "/mnt/data_disk/projects/all_subj/surfaceProj/afni/localizerExp/surfAnalysis/"+surfSubjName+"/"+surfSubjName+".surf.results/stats."+surfSubjName+"."+hemi+".1D.dset"
    statsData = pd.DataFrame(data=map(float,readStatsData(infileDir)))

    roiFileName = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName+"/SUMA/"+hemi+"+Parahip+Lingual+fusifor.1D"
    roiNodes = readRoiNodes(roiFileName)
    roiNodes = np.array(map(int, roiNodes))

    roi = np.zeros(statsData.shape[0])
    for i in roiNodes:
            roi[i] = 1
    nodes = range(0,statsData.shape[0])       
    statsData.insert(1,'nodes', nodes) 

    statsData.insert(1,'roi', roi)
    statsData.columns = ["val","roi","nodes"]
    maxNum = statsData[statsData.roi == 1].val.max(axis=0)
    minNum = statsData[statsData.roi == 1].val.min(axis=0)

    # maxAll = statsData.val.max(axis=0)
    # minAll = statsData.val.min(axis=0)

    maxIndex = statsData[(statsData.loc[:,"val"] == maxNum)].nodes
    minIndex = statsData[(statsData.loc[:,"val"] == minNum)].nodes
    return maxIndex,minIndex


for s in range(0,len(fsSubjName)):
    for h in range(len(hemi)):
        maxIndex,minIndex = getMaxMinNodes(hemi[h],fsSubjName[s],surfSubjName[s])
        print fsSubjName[s],maxIndex,"\n",minIndex


# In[13]:

#open matlab ,dse the Euclidean distance to draw a line(40 vertices) between this two vertex, so that I get 40 vertices,
#use the freesurfer 2-dimention flat data(eg,lh.full.flat.patch.3d) to compute the Euclidean distance,
#then I got five vertices which are nearest to each vertex separately,

import matlab.engine
eng = matlab.engine.start_matlab()

for s in range(0,len(fsSubjName)):
    for h in range(len(hemi)):
        maxIndex,minIndex = getMaxMinNodes(hemi[h],fsSubjName[s],surfSubjName[s])
#         print maxIndex,minIndex
        ret = eng.writeDivideNodes(int(maxIndex.index.values),int(minIndex.index.values),hemi[h],fsSubjName[s])
#         print(ret)
