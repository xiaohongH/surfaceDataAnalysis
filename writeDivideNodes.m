function [ XindexTovnoList ] = writeDivideNodes( nodes1,nodes2,hemi,subName)
%this function mean to fraw a line between nodes1 and nodes2 in 2 dimension
%surface---lh or rh full.flat.patch.3d
%

addpath('/usr/local/freesurfer/matlab');
% 把2d平面的上的(x,y)坐标，转换成surface上的vertex;
% 找到patch_coor.x坐标对应的索引；
% 根据索引找到patch_coor.vno的值，即具体的vertex的值，

fileName = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/surf/',hemi,'.full.flat.patch.3d']
patch_coor = read_patch(fileName);

%将vertex的number转换成成xy坐标
vertex_index = find(patch_coor.vno == nodes1);
x1 = patch_coor.x(:,vertex_index:vertex_index);
y1 = patch_coor.y(:,vertex_index:vertex_index);

vertex_index = find(patch_coor.vno == nodes2);
x2 = patch_coor.x(:,vertex_index:vertex_index);
y2 = patch_coor.y(:,vertex_index:vertex_index);

% totalDistance=sum(bsxfun(@minus,[x1,y1],[x2,y2]).^2,2); 

%求一元一次方程式
% 把线段分成divideNum--n等分，一共有divideNum+1个点的坐标；


totalDistance = sqrt(abs(x1-x2).^2 + abs(y1-y2).^2);
% % divideNum = fix(totalDistance/2);%根据距离划分多少个roi
divideNum = 20;%固定分为20个roi
ousideNum = 10;

partDistance = totalDistance/divideNum;
partX = (x1-x2)/divideNum;
partY = (y1-y2)/divideNum;

xlist = []
ylist = []



for i = -ousideNum:divideNum+ousideNum+1
    xlist = [xlist,x1-i*partX];
    ylist = [ylist,y1-i*partY];
end

% 求出所有的vertex
XindexTovnoList = [];
for i = 1:divideNum+2*ousideNum+1
    x = xlist(:,i:i);
    y = ylist(:,i:i);
    contrastList = abs(patch_coor.x -x);
    sortconList = sort(contrastList);
    kcontrastValue = sortconList(:,1:100);
    Xvalue = [];
    XToYvalue = [];
    Xindex = [];
    for j = kcontrastValue
        [row,Xcolumn]=find(contrastList==j);
        for k = length(Xcolumn)
            Xvalue = [Xvalue;patch_coor.x(:,Xcolumn(:,k:k):Xcolumn(:,k:k))];
            Xindex = [Xindex;Xcolumn(:,k:k)];
            XToYvalue =[XToYvalue;patch_coor.y(:,Xcolumn(:,k:k):Xcolumn(:,k:k))];
        end
    end
    %找到和y坐标最近的值
    contrastList = abs(XToYvalue - y);
    [YconListrow,Yconlistcolumn]=find(contrastList==min(min(contrastList)));
    coorColumn = Xindex(YconListrow:YconListrow,:); 
    % 二维坐标
    tkrx = patch_coor.x(:,coorColumn:coorColumn);
    tkry = patch_coor.y(:,coorColumn:coorColumn);

    % 二维坐标对应的vertex
    XindexTovnoList = [XindexTovnoList,patch_coor.vno(:,coorColumn:coorColumn)];
end

XindexTovnoList = XindexTovnoList'
combineAllNodes = []
%%
v = [patch_coor.x;patch_coor.y];
vno = patch_coor.vno;

% surffn = '/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/mm/surf/lh.full.flat.patch.3d.asc'
% % surffn = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/surf/',hemi,'.pial.asc']
% % 
% [v,f]=freesurfer_asc_load(surffn); % load surface 

nv=size(v,1); % number of vertices 
for idx=1:numel(XindexTovnoList)
    centerNode = XindexTovnoList(idx)
    centerNode = find(patch_coor.vno == centerNode)
    %%

%     if size(v,1)~=3, v=v'; end
%     D=surfing_eucldist(v(:,centerNode),v)';
    vidxs=(1:size(v,2))'; % all vertex indices
    xs = v(:,centerNode);
    ys = v;
    [three1,n1]=size(v(:,centerNode));
    [three2,n2]=size(v);

    D=zeros(n1,n2);
    for k=1:n1
        D(k,:)=sqrt(sum((repmat(xs(:,k),1,n2)-ys).^2))';
    end
    D = D'
    
    [dummy,is]=sort(D,'ascend');
    issel=is(1:5);
    aroundidxs=vno(issel)';
    selidxs=issel;
%     aroundidxs=vidxs(selidxs)';
    aroundidxs=vno(selidxs)';
    %%
    
    nodesFileName = ['newNodes_',hemi,'_SurfCoord.',string(XindexTovnoList(idx)),'_',idx,'.1D'];
    nodesFileName = join(nodesFileName,string(''));
    outNodesFilePath = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',char(subName),'/SUMA/',char(nodesFileName)];
%     outNodesFileName = join(outNodesFilePath,string(''));
%     aroundidxs = aroundidxs'
    save(outNodesFilePath,'aroundidxs','-ascii');
    combineAllNodes = [combineAllNodes,aroundidxs'];
end
% [combineAllNodes,is]=sort(combineAllNodes,'ascend');

%%
combineAllNodes = combineAllNodes'
outFileName =['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/SUMA/nodelocations_',hemi,'.1D']
combineAllNodesFileName = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/SUMA/allnodelocations_',hemi,'.1D']

save(outFileName,'XindexTovnoList','-ascii');

save(combineAllNodesFileName,'combineAllNodes','-ascii');
% f = fopen(combineAllNodesFileName,'wt'); 
% fprintf(f,'%d\n',combineAllNodes); 
% fclose(f);
end

