#surf.loc.proc.py
cd /mnt/data_disk/projects/all_subj/surfaceProj/afni/localizerExp/surfAnalysis

#ec kj ls mm pk ta
for sub in kj;do

  cd   ${sub}
  echo ${sub}

afni_proc.py -subj_id ${sub}.surf \
	-scr_overwrite       \
	-blocks tshift align volreg surf blur scale regress      \
	-copy_anat ${sub}/anat+orig                               \
	-dsets ${sub}/loc?+orig.HEAD                            \
	-surf_anat /mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/${sub}/SUMA/${sub}_SurfVol.nii                        \
	-surf_spec /mnt/data_disk/projects/all_subj/surfaceProj/surfaceFreesurferAnat/bingFreesurfer/${sub}/SUMA/${sub}_?h.spec                     \
	-volreg_align_to third                                   \
	-volreg_align_e2a                                        \
	-blur_size 6                                             \
	-regress_stim_times ${sub}/stimuli/FH1_face.txt ${sub}/stimuli/FH2_house.txt        \
	-regress_stim_labels face house                             \
	-regress_basis 'BLOCK(16,1)'                             \
	-regress_censor_motion 0.3                               \
	-regress_opts_3dD                                        \
		-jobs 2                                              \
		-gltsym 'SYM: face -house' -glt_label 1 F-H	\
	-execute  
  cd ../
done
cd ../
