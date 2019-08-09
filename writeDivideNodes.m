function [ XindexTovnoList ] = writeDivideNodes( nodes1,nodes2,hemi,subName)
%compute 20 equal distance points between these two nodes,in 2 dimension surface---lh/rh full.flat.patch.3d;
% then find the nearest five nodes to each nodes and write to.1D file.

%nodes1 -- the vertex in FFA or PPA;
%nodes2 -- the vertex in FFA or PPA;
%hemi -- lh/rh
%subName -- the subject Name

%XindexTovnoList -- the 20 vertices

addpath('/usr/local/freesurfer/matlab');
% use the freesurfer 2-dimention flat data: lh.full.flat.patch.3d to compute the Euclidean distance,
fileName = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/surf/',hemi,'.full.flat.patch.3d']
patch_coor = read_patch(fileName);

%find the correspond x-y-coordinates of the nodes
vertex_index = find(patch_coor.vno == nodes1);
x1 = patch_coor.x(:,vertex_index:vertex_index);
y1 = patch_coor.y(:,vertex_index:vertex_index);

vertex_index = find(patch_coor.vno == nodes2);
x2 = patch_coor.x(:,vertex_index:vertex_index);
y2 = patch_coor.y(:,vertex_index:vertex_index);

% totalDistance=sum(bsxfun(@minus,[x1,y1],[x2,y2]).^2,2); 
%compute 20 equal distance points according x-y-coordinates
totalDistance = sqrt(abs(x1-x2).^2 + abs(y1-y2).^2);
% % divideNum = fix(totalDistance/2);
divideNum = 20;
ousideNum = 0;

partDistance = totalDistance/divideNum;
partX = (x1-x2)/divideNum;
partY = (y1-y2)/divideNum;

xlist = []
ylist = []

for i = -ousideNum:divideNum+ousideNum+1
    xlist = [xlist,x1-i*partX];
    ylist = [ylist,y1-i*partY];
end

% convert all the x-y-coordinates to vertices 
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

    contrastList = abs(XToYvalue - y);
    [YconListrow,Yconlistcolumn]=find(contrastList==min(min(contrastList)));
    coorColumn = Xindex(YconListrow:YconListrow,:); 

    tkrx = patch_coor.x(:,coorColumn:coorColumn);
    tkry = patch_coor.y(:,coorColumn:coorColumn);

    % the x-y-coordinates to vertices 
    XindexTovnoList = [XindexTovnoList,patch_coor.vno(:,coorColumn:coorColumn)];
end

XindexTovnoList = XindexTovnoList'
combineAllNodes = []

v = [patch_coor.x;patch_coor.y];
vno = patch_coor.vno;
nv=size(v,1); % number of vertices 

% use the freesurfer 2-dimention flat data: lh.full.flat.patch.3d to compute the Euclidean distance,
% then I got five vertices which are nearest to centerNode,

for idx=1:numel(XindexTovnoList)
    centerNode = XindexTovnoList(idx)
    centerNode_index = find(patch_coor.vno == centerNode)

%     if size(v,1)~=3, v=v'; end
%     D=surfing_eucldist(v(:,centerNode),v)';

% according the Euclidean distance to compute the nearest five vertices,

    vidxs=(1:size(v,2))'; % all vertex indices
    xs = v(:,centerNode_index);
    ys = v;
    [three1,n1]=size(v(:,centerNode_index));
    [three2,n2]=size(v);

    D=zeros(n1,n2);
    for k=1:n1
        D(k,:)=sqrt(sum((repmat(xs(:,k),1,n2)-ys).^2))';
    end
    D = D'
    
    [dummy,is]=sort(D,'ascend');
    issel=is(1:5);
    aroundidxs=vno(issel)';
    
    nodesFileName = ['newNodes_',hemi,'_SurfCoord.',string(XindexTovnoList(idx)),'_',idx,'.1D'];
    nodesFileName = join(nodesFileName,string(''));
    outNodesFilePath = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',char(subName),'/SUMA/',char(nodesFileName)];
%     outNodesFileName = join(outNodesFilePath,string(''));
%     aroundidxs = aroundidxs'
    save(outNodesFilePath,'aroundidxs','-ascii');
    combineAllNodes = [combineAllNodes,aroundidxs'];
end
% [combineAllNodes,is]=sort(combineAllNodes,'ascend');

combineAllNodes = combineAllNodes'
outFileName =['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/SUMA/nodelocations_',hemi,'.1D']
combineAllNodesFileName = ['/mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/',subName,'/SUMA/allnodelocations_',hemi,'.1D']
save(outFileName,'XindexTovnoList','-ascii');
save(combineAllNodesFileName,'combineAllNodes','-ascii');

end

