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
        StateDef = inflated_lh
        StateDef = inflated_rh
        StateDef = occip.patch.3d
        StateDef = occip.patch.flat_lh
        StateDef = occip.patch.flat_rh
        StateDef = occip.flat.patch.3d_lh
        StateDef = occip.flat.patch.3d_rh
        StateDef = fusiform.patch.flat_lh
        StateDef = fusiform.patch.flat_rh
        StateDef = full.patch.3d
        StateDef = full.patch.flat_lh
        StateDef = full.patch.flat_rh
        StateDef = full.flat.patch.3d_lh
        StateDef = full.flat.patch.3d_rh
        StateDef = full.flat_lh
        StateDef = full.flat_rh
        StateDef = flat.patch_lh
        StateDef = flat.patch_rh
        StateDef = sphere_lh
        StateDef = sphere_rh
        StateDef = white
        StateDef = sphere.reg_lh
        StateDef = sphere.reg_rh
        StateDef = rh.sphere.reg_lh
        StateDef = rh.sphere.reg_rh
        StateDef = lh.sphere.reg_lh
        StateDef = lh.sphere.reg_rh
        StateDef = pial-outer-smoothed
        StateDef = inf_200

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.smoothwm.gii
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3
        Anatomical = Y
        LabelDset = lh.aparc.a2009s.annot.niml.dset

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.pial.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.inflated.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = inflated_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.full.patch.3d.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = full.patch.3d
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.full.flat.patch.3d.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = full.flat.patch.3d_lh
        EmbedDimension = 2
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.sphere.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = sphere_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.white.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = white
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.sphere.reg.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = sphere.reg_lh
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = lh.inf_200.gii
        LocalDomainParent = lh.smoothwm.gii
        SurfaceState = inf_200
        EmbedDimension = 3
        Anatomical = N

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
        SurfaceState = inflated_rh
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
        SurfaceState = full.flat.patch.3d_rh
        EmbedDimension = 2
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere_rh
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
        SurfaceState = sphere.reg_rh
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

