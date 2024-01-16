
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
