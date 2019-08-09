# surfaceDataAnalysis
This project mean to automatically draw a line between two anatomic areas. 

# 1, freesurfer_anatomicData_preprocessing:
use recon-all 

# 2, Cutting inflated FreeSurfer surfaces: 
use tksurfer provided by freesurfer

# 3, surf.loc.proc.py: 
afni surface-based epi data preprocessing

# 4, labelToCoordinate.py: 
  create a big mask(cover the FFA and PPA);
  compute the maximun and the minimum value of the t-test statistic data;
  find the correspond vertices of the maximun and the minimum t value -- two nodes;
  
  compute 20 equal distance points between these two nodes,in 2 dimension surface---lh/rh full.flat.patch.3d 
  then find the nearest five nodes to each nodes and write to.1D file.
  
# 5, writeDivideNodes.m: 
  compute 20 equal distance points between these two nodes,in 2 dimension surface---lh/rh full.flat.patch.3d 
  then find the nearest five nodes to each nodes and write to.1D file.
  
# 6, drawROI.py: 
convert all the .1D file to .dset file, so that can read in SUMA.
  
# 7, localizeData.py
  use the above .1D file(20 .1D file, each file contains five nodes) to extract blur epi data.

