# `prevampire`

![GitHub](ADDHERE)
[![Documentation Status](ADDHERE)](ADDHERE)
![PyPI](ADDHERE)

PREVAMPIRE is a package made to work in supplementary with the [VAMPIRE package](https://github.com/tengjuilin/vampire-analysis). This package contains methods that expedite the user's preparation for the VAMPIRE pipeline, and limits the amount of code interaction needed for someone new to python. 

The package was made to turn raw tif images of microglia into numpy arrays so that the vampire package could be applied succesfully. This package also applies and outputs skeletonization on the images after thresholding. 

The VAMPIRE package returns a dataframe containing characteristics of each microglia identified within the dataset and return average shape modes. 

Cell morphology is used as a support to show the effectivity of therapudics.   

## Installation

If Python is installed on your machine, type the following line into your command prompt to install via [PyPI](ADDHERE):

```bash
pip install vampire-analysis
```

Otherwise, fork the package to ... **ASK NELS**

## Getting started

Create a file which has all the .tif images you want to analyze.

```python
import prevampire as pv  # recommended import signature
raw_dir = 'file/path'  # file path to .tif images
```

## Applying PREVAMPIRE Package

Below are a list of methods you want to apply to get to the desired skeletonization and vampire df and shape modes. Check out [prevampire.py](https://github.com/onoderamia/prevampire/blob/main/prevampire/prevampire.py) for more in depth method comments. 

For a specific dataset, the code uses two .npy arrays to keep track of images while applying thresholding and skeletonization. The image array and the name array. These two arrays are always returned in a specific method. 

To go more in depth to skeletonization, check out the [Skan package](https://skeleton-analysis.org/stable/index.html#) used to find the method desired. 

 ```python

max_imgs, org_names = pv.take_channel(raw_dir, print_image = 1) # maximize image to only include iba

threshall_dir = 'new/file/path' # new file
pv.apply_and_save_all_thresholds(max_imgs, org_names, threshall_dir) # apply all thresholds to a specific subset in the dataset and save them to a defined directory

thresh_imgs, thresh_names = pv.apply_threshold(max_imgs, org_names, label = 'label', method = 'method' print_image = 1) # apply chosen threshold to maximized images (defaults to li)

skel_imgs, skel_names = pv.skeletonize_images(thresh_imgs, thresh_names, print_image = 1) 

skel_df = pv.get_skel_df(skel_imgs, skel_name, show = 1) # get dataframe for skeletonized images

```

Below are a list of supplementary methods you can use throughout the prevampire pipeline. 

 ```python

thresh_tif_dir = 'new/new/file/path' # new file
pv.save_tif(thresh_imgs, thresh_names, thresh_tif_dir) # save .npy arrays as .tif images in a defined directory

thresh_npy_dir = 'new/new/new/file/path' # new file
pv.save_npy(thresh_imgs, thresh_names, thresh_npy_dir) # save .npy arrays as .npy arrays in a defined directory

thresh_imgs, thresh_names = pv.load_tif_imgs(thresh_tif_dir) # load .tif images as .npy arrays in a defined directory

thresh_imgs, thresh_names = pv.load_npy_imgs(thresh_npy_dir) # load .npy arrays as .npy arrays in a defined directory

pv.display_img_side(thresh_imgs, skel_imgs, 0, 'thresh', 'skel') # put images from respective .npy arrays side to side for comparison

output_dir = 'new/new/new/new/file/path' # new file
pv.save_df(skel_df, 'skel_df', output_dir) # save dataframe in defined directory

```

## Applying to VAMPIRE package

Once you get the thresholded images and names, you can then choose to apply these images to the [VAMPIRE package](https://vampire.readthedocs.io/en/latest/index.html). 

 ```python

import vampire as vp
from vampire import quickstart

## Get VAMPIRE dataframe
copy_thresh_arr = thresh_imgs.copy()
copy_thresh_arr = [item.astype('uint8') for item in copy_thresh_arr] # change to compatible type
vampire_df = vp.extraction.extract_properties_from_img_set(copy_thresh_arr, thresh_names) # get df
pv.save_df(vampire_df, 'vampire_df', output_dir) # saved as .csv file (optionial)

## Get VAMPIRE shape mode
build_info_df = pd.DataFrame({
    'img_set_path': [thresh_tif_dir], # define image directory
    'output_path': [output_dir], # define output directory; saved as .png and .pickle file
    'model_name': ['NAME'],
    'num_points': [np.nan],
    'num_clusters': [np.nan],
    'num_pc': [np.nan],
})

quickstart.build_models(build_info_df, random_state=1) # get shape mode

```

## Method parameters and returns

### pv.remove_files(file_dir, delete)
	Remove specific files from a given file directory.
Parameters:
  - file_dir (str): The directory to remove files from.
  - delete (str): Substring to match files for deletion.

### pv.move_files(file_dir, target_dir, takeout)
	Move specific files from one directory to another.
Parameters:
   - file_dir (str): The directory to take files from.
   - takeout (str): Substring to match files to take out.
   - target_dir (str): The directory to place files in.


### pv.take_channel(img_dir, print_image = 0)
Process images from a given directory, creating maximum intensity projections.
Parameters:
  - img_dir (str): The directory containing raw tif images.
  - print_image (int, optional): Number of images to display. Defaults to 0.

Returns:
   - tuple: A tuple containing two elements:
       - result_images (list): A list of 2D arrays representing maximum intensity projection images.
       - img_name_list (list): A 1D array of corresponding image names.

### pv.save_npy(img_arr, img_name_list, save_location)
Save NumPy arrays as .npy files in the specified location.
Parameters:
   - img_arr (list): A list of NumPy arrays representing images.
   - img_name_list (list): A list of image names corresponding to the arrays.
   - save_location (str): The directory where the .npy files will be saved.

### pv.save_tif(img_arr, img_name_list, save_location)
Save images as .tif files in the specified location.
Parameters:
   - img_arr (list): A list of NumPy arrays representing images.
   - img_name_list (list): A list of image names corresponding to the arrays.
   - save_location (str): The directory where the .tif files will be saved.

### pv.load_npy_imgs(directory)
Load files from a given directory of .npy files.
   	Parameters:
   - directory (str): The directory containing files.
   	Returns:
   - list: A list of loaded NumPy arrays or images.

### pv.load_tif_imgs(directory)
Load files from a given directory of .tif files.
  	Parameters:
   - directory (str): The directory containing files.
  	Returns:
   - list: A list of loaded NumPy arrays or images.

### pv.apply_and_save_all_thresholds(img_arr, img_name_list, output_dir, num_imgs = 5)
Apply various thresholding methods and save the results as .tif files.
Parameters:
   - img_arr (list): A list of NumPy arrays representing the intensified images.
   - img_name_list (list): A list of image names corresponding to the arrays.
   - output_dir (str): The directory where the thresholded images will be saved.
   - num_imgs (int, optional): The number of images to select for thresholding and saving. Defaults to 5.

### pv.apply_threshold(img_arr, img_name_list, label = 'threshli', method = 'li', print_image = 0)
Apply a thresholding method to a list of images and return segmented images.
  	Parameters:
   - img_arr (list): A list of NumPy arrays representing the indensified images.
   - img_name_list (list): A list of image names corresponding to the arrays.
   - label (str, optional): A label to append to the segmented image names. Defaults to 'threshli'.
   - method (str, optional): The thresholding method to use. Defaults to 'li'.
Other Options: {'otsu', 'yen', 'isodata', 'minimum', 'mean', 'triangle'}
   - print_image (int, optional): Number of segmented images to display. Defaults to 0.

   	Returns:
   - tuple: A tuple containing two elements:
       - segmented_images (list): A list of segmented images.
       - seg_name_list (list): A list of corresponding segmented image names.

### pv.skeletonize_images(thresh_arr, img_name_list, label = 'skel', print_image = 0)
Skeletonize a list of binary images and return the skeletonized images.
Parameters:
   - thresh_arr (list): A list of thresholded binary images.
   - img_name_list (list): A list of image names corresponding to the arrays (use the name list from take_channel).
   - label (str, optional): A label to append to the skeletonized image names. Defaults to 'skel'.
   - print_image (int, optional): Number of skeletonized images to display. Defaults to 0.

Returns:
   - tuple: A tuple containing two elements:
       - skel_imgs (list): A list of skeletonized images.
       - skel_name_list (list): A list of corresponding skeletonized image names.

### pv.display_img_side(array1, array2, index, label1, label2)
Display two images side by side for visual comparison.
Parameters:
   - array1 (list): A list of images or arrays.
   - array2 (list): Another list of images or arrays.
   - index (int): Index of the images to display.
   - label1 (str): Label for the first set of images.
   - label2 (str): Label for the second set of images.

Returns:
   - None: Displays the images using Matplotlib.

### pv.get_skel_df(skel_arr, skel_name_list, show = 0)
Process a list of skeletonized images, extract properties, and display branch types.
   Parameters:
   - skel_arr (list): A list of skeletonized images or arrays.
   - skel_name_list (list): A list of names corresponding to the skeletonized images.
   - show (int, optional): The number of images to display branch types. Defaults to 0.

   Returns:
   - pd.DataFrame: A Pandas DataFrame containing skeletonization properties.

### pv.save_df(dataframe, name, output_dir)
Save dataframe as a .csv file.
   Parameters:
   - dataframe (pandas df): The directory containing files.
   - name (String): Name of dataframe.
   - output_dir (String): Directory to be saved.

## References
[1] Lin, O. VAMPIRE, (2020), GitHub repository, https://github.com/tengjuilin/vampire-analysis

[2] Lin, C. (2021). Skeletonization and fractal analysis of microglial cells in the neonatal brain. [Doctoral dissertation, University of Washington]. ResearchWorks Archive at the University of Washington. https://digital.lib.washington.edu/researchworks/bitstream/handle/1773/47957/Lin_washington_0250O_23542.pdf?sequence=1&isAllowed=y

[3] Juan Nunez-Iglesias, Adam J. Blanch, Oliver Looker, Matthew W. Dixon, and Leann Tilley. A new Python library to analyse skeleton images confirms malaria parasite remodelling of the red blood cell membrane skeleton. PeerJ, 6:e4312, 2018. doi:10.7717/peerj.4312.

