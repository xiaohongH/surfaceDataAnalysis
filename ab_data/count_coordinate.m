addpath('/usr/local/freesurfer/matlab');

% 把2d平面的上的(x,y)坐标，转换成surface上的vertex;
% 找到patch_coor.x坐标对应的索引；
% 根据索引找到patch_coor.vno的值，即具体的vertex的值，
% 
patch_coor = read_patch(string('/home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/surf/lh.full.flat.patch.3d'))
[sur_v,suf_f] = read_surf(string('/home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/surf/lh.white'))

% 1,freesurfer上做的contrast是基于fsavereage的，需要将fsaverage上的坐标转换到x,y,z坐标上，
% 将ffa ppa的vertex的坐标转换成x,y的坐标;
% 2,将afni上的坐标转换到fsaverage上

x1 = 70.0489;
y1 = 150.2784;

x2 = 106.876;
y2 = 135.0754;

%求一元一次方程式
% 把线段分成5等分，一共有6个点的坐标；
totalDistance = sqrt(abs(x1-x2).^2 + abs(y1-y2).^2);
partDistance = totalDistance/5;
partX = abs(x1-x2)/5;
partY = abs(y1-y2)/5;

xlist = x1
ylist = y1
for i = 1:5
    xlist = [xlist,x1+i*partX];
    ylist = [ylist,y1+i*partY];
end

for i = 1:6
    x = xlist(:,i:i);
    y = ylist(:,i:i);
   
end
contrastList = abs(patch_coor.x - x);
sortconList = sort(contrastList);
kcontrastValue = sortconList(:,1:100);
Xvalue = [];
XToYvalue = [];
Xindex = [];
for i = kcontrastValue
    [row,Xcolumn]=find(contrastList==i);
    Xvalue = [Xvalue;patch_coor.x(:,Xcolumn:Xcolumn)];
    Xindex = [Xindex;Xcolumn];
    XToYvalue =[XToYvalue;patch_coor.y(:,Xcolumn:Xcolumn)];
end
    
% [row,Xcolumn]=find(contrastList==min(min(contrastList)));
% Xvalue = patch_coor.x(:,Xcolumn:Xcolumn);
% XToYvalue = patch_coor.y(:,Xcolumn:Xcolumn);

%找到和y坐标最近的值
contrastList = abs(XToYvalue - y);
[YconListrow,Yconlistcolumn]=find(contrastList==min(min(contrastList)));
coorColumn = Xindex(YconListrow:YconListrow,:);

% 二维坐标
tkrx = patch_coor.x(:,coorColumn:coorColumn);
tkry = patch_coor.y(:,coorColumn:coorColumn);

% 二维坐标对应的vertex
XindexTovno = patch_coor.vno(:,coorColumn:coorColumn);

% XindexTovno = double(str2num(XindexTovno))
% [m,n] = find(patch_/coor.vno == 32946);
% XindexTovno = 4544;
vnoTotkRAS = sur_v(XindexTovno+1:XindexTovno+1,:);

% command = 'mri_info --vox2ras /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/mri/orig/001.mgz';
% [status,anatNorig]= system(command,'-echo');
% command = 'mri_info --vox2ras /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/mri/orig.mgz';
% [status,T1Norig]= system(command,'-echo');
% command = 'mri_info --tkr2scanner /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/mri/orig.mgz';
% [status,tkr2scanner]= system(command,'-echo');

command = 'mri_info --vox2ras-tkr /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/mri/orig.mgz';
[status,Torig]= system(command,'-echo');
command = 'mri_info --ras2vox-tkr /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/mri/orig.mgz';
[status,ras2voxtkr]= system(command,'-echo');

Torig = double(str2num(Torig))
ras2voxtkr = double(str2num(ras2voxtkr))

% anatNorig = double(str2num(anatNorig))
% T1Norig = double(str2num(T1Norig))
% tkr2scanner = double(str2num(tkr2scanner))


% tkrR =36.53;
% tkrA =-27.52;
% tkrS =-27.35;
% 把2d平面的上的(x,y)坐标，转换成surface上的vertex;
% 把vertex上的坐标转换成CRS(volume index);
% 然后把volume index的坐标转换成原始图像的RAS坐标
%把freesurfer 上的RAS坐标转换成AFNI上的LPS坐标（RPI）

% T1volumeIndex = inv(Torig)*[tkrR tkrA tkrS 1]';
tkRASTovolumeIndex = inv(Torig)*[vnoTotkRAS 1]';
volumeIndexTofsRAS = inv(ras2voxtkr)*tkRASTovolumeIndex;
volumeIndexTofsRAS(1:2,:) = -volumeIndexTofsRAS(1:2,:);
fsRASafniLIP = volumeIndexTofsRAS;


% ScannerRAS = anatNorig*inv(Torig)*[tkrR tkrA tkrS 1]';
% tkr2ras = tkr2scanner*[tkrR tkrA tkrS 1]';
% anatNorig(1:2,:) = -anatNorig(1:2,:);
% ScannerRSP = T1Norig*inv(Torig)*[tkrR tkrA tkrS 1]';
% v_indexToras = inv(ras2voxtkr)*[92 156 101 1]';

