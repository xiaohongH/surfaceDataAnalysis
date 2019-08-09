#!/usr/bin/env python
# coding: utf-8

# In[11]:


hemi = ["rh","lh"]

fsSubjName = ["ab_data","bg_data","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]
surfSubjName = ["ab","bg","ec","kj","lh","ls","mm","pk","ta","ts","xy","zb"]

# fsSubjName = ["ab_data"]
# surfSubjName = ["ab"]


# In[5]:


#recon-all之后的结构像，再将全脑分成不同的脑区
#将lh.aparc.annot分割成一个一个的label，每一个label中的值是都是一个一个的vertex
#jupyter 要在bash下打开才能执行
import subprocess

# fsSubjName = ["lh"]
# surfSubjName = ["lh"]

for s in range(0,len(fsSubjName)):
    inFileName = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer"
    outFileName = "/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/"+fsSubjName[s]+"/SUMA/"


    for h in hemi:
        command1 = "mkdir "+outFileName+h+"\\"
        print command1
        subprocess.call(command1,shell = True)

        command = "bash;        mri_annotation2label --subject "+fsSubjName[s]+" --hemi "+h+"         --annotation  aparc.a2009s         --outdir "+outFileName+h

        print command
        subprocess.call(command,shell = True)
        #将1D文件转成dset文件
    #     ConvertDset -o_1D -add_node_index -input lh+fusiform+parahippocampal.1D -prefix lh+fusiform+parahippocampal


# In[7]:


#合并多个label的值;用作mask，求出这个mask内的看face和house的最大最小值
#并将多个label中vertex的值提取出来
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


#将合并的label，从1D转成.dset文件
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


#将localizer stast.niml.dset的数据转成1D.dset的数据
import os
import subprocess
hemi = ["lh","rh"]
for s in range(0,len(fsSubjName)):
    filePath = "/mnt/data_disk/projects/all_subj/surfaceProj/afni/localizerExp/surfAnalysis/"+surfSubjName[s]+"/"+surfSubjName[s]+".surf.results/"
    for h in hemi:
        command = "cd "+filePath+";        ConvertDset -o_1D -input "+filePath+"/stats."+surfSubjName[s]+".surf."+h+".niml.dset"+" -prefix stats."+surfSubjName[s]+"."+h
        print command
        subprocess.call(command, shell=True)


# In[12]:


#求出tempole中，stats对看face和house激活最大最小的vertex的值
#extract label中的数据，并求出stat中，在templobe 这个roi内的，最大最小值对应的nodes的值
#求出 FFA和PPA的坐标
#vertex num从0开始
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



hemi = ["lh","rh"]
# fsSubjName = ["ls"]
# surfSubjName = ["ls"]
for s in range(0,len(fsSubjName)):
    for h in range(len(hemi)):
        maxIndex,minIndex = getMaxMinNodes(hemi[h],fsSubjName[s],surfSubjName[s])
        print fsSubjName[s],maxIndex,"\n",minIndex


# In[13]:


#打开matlab，将两点之间的nodes，分割成好几部分，并连线
import matlab.engine
eng = matlab.engine.start_matlab()

for s in range(0,len(fsSubjName)):
    for h in range(len(hemi)):
        maxIndex,minIndex = getMaxMinNodes(hemi[h],fsSubjName[s],surfSubjName[s])
        print maxIndex,minIndex
        ret = eng.writeDivideNodes(int(maxIndex.index.values),int(minIndex.index.values),hemi[h],fsSubjName[s])
        print(ret)
#         writeDivideNodes(42959,41677,'rh','ab_data',[10])


# In[ ]:





# In[ ]:




