import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

import os

# handle exception ! 
path_in_nifi = os.environ['path_in_nifi']
path_out_npy = os.environ['path_out_npy']
path_out_image = os.environ['path_out_image']


def to_npy():
    # refactor output name to a more human readable format
    for file in os.listdir(path_in_nifi):
        if file.endswith(".nii.gz"):
            img = nib.load(f'{path_in_nifi}/{file}')
            data = img.get_fdata()

            for i in range(data.shape[2]):
                slice2D = data[:, :, i]
                np.save(f'{path_out_npy}/{file}-s{i}', slice2D)

def to_img():
    # refactor output name to a more human readable format
    for file in os.listdir(path_in_nifi):
        if file.endswith(".nii.gz"):
            img = nib.load(f'{path_in_nifi}/{file}')
            data = img.get_fdata()

            for i in range(data.shape[2]):
                slice2D = data[:, :, i]
                plt.imshow(slice2D ,cmap = 'gray')
                plt.savefig(f'{path_out_image}/{file}-s{i}.png')




def main():
    to_img()


if __name__ == "__main__":
    main()