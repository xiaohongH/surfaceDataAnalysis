# delimits comments

# Creation information:
#     user    : hh
#     date    : 2019年 05月 30日 星期四 18:51:51 CST
#     machine : hh-QiTianM415-D004
#     pwd     : /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data/SUMA
#     command : @SUMA_Make_Spec_FS -NIFTI -fspath /home/hh/study/python/code/ml/nipype_tutorial/bingfreesurfer/ab_data -sid ab_data

# define the group
        Group = ab_data

# define various States
        StateDef = smoothwm
        StateDef = pial
        StateDef = inflated
        StateDef = occip.patch.3d
        StateDef = occip.patch.flat
        StateDef = occip.flat.patch.3d
        StateDef = fusiform.patch.flat
        StateDef = full.patch.3d
        StateDef = full.patch.flat
        StateDef = full.flat.patch.3d
        StateDef = full.flat
        StateDef = flat.patch
        StateDef = sphere
        StateDef = white
        StateDef = sphere.reg
        StateDef = rh.sphere.reg
        StateDef = lh.sphere.reg
        StateDef = pial-outer-smoothed
        StateDef = inf_200

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.smoothwm.gii
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3
        Anatomical = Y
        LabelDset = rh.aparc.a2009s.annot.niml.dset

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.pial.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inflated.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inflated
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.full.patch.3d.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = full.patch.3d
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.full.flat.patch.3d.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = full.flat.patch.3d
        EmbedDimension = 2
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.white.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = white
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.reg.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere.reg
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inf_200.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inf_200
        EmbedDimension = 3
        Anatomical = N

