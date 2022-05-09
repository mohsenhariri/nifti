import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

import os

# handle exception ! 
path_in_nifi = os.environ['path_in_nifi']
path_out_npy = os.environ['path_out_npy']



# refactor output name to a more human readable format
for file in os.listdir(path_in_nifi):
    if file.endswith(".nii.gz"):
        img = nib.load(f'{path_in_nifi}/{file}')
        data = img.get_fdata()

        for i in range(data.shape[2]):
            slice2D = data[:, :, i]
            np.save(f'{path_out_npy}/{file}-s{i}', slice2D)

