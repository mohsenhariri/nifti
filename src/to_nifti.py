import os
import nibabel as nib
import numpy as np

# handle exception ! 
path_in_nifi = os.environ['path_in_nifi']
path_in_npy = os.environ['path_out_npy']
path_out_nifit = os.environ['path_out_nifit']


data_indices = [485]
# for idx in data_indices_raw:
#     data_indices.append(idx.replace('BRATS_', ''))


print(data_indices)


# exit()
# data_indices = [305]
def to_nifti_train():
    for data_idx in data_indices:
        for mo in range(4):
            nifti_name = f'BRATS_{data_idx}_000{mo}.nii.gz'
            c = []
            for slice_idx in range(151):
                # sr_path = f'BRATS_{data_idx}_000{mo}.nii.gz-s{slice_idx}_out.npy' # super resolution
                sr_path = f'BRATS_{data_idx}_000{mo}.nii.gz-s{slice_idx}.npy'

                m2x2 = np.load(f'{path_in_npy}/{sr_path}')
                c.append(m2x2)
            tensor = np.asarray(c)
            print(tensor.shape)
            img_lr = nib.load(f'{path_in_nifi}/BRATS_{data_idx}_000{mo}.nii.gz')
            data_nii_full = nib.Nifti1Image(tensor, img_lr.affine)
            # data_nii_full = nib.Nifti1Image(ttt, np.eye(4))   
            nib.save(data_nii_full, f'{path_out_nifit}/{nifti_name}')


def to_nifti_label():
    print('label')
      



def main():
    to_nifti_train()

if __name__ == "__main__":
    main()