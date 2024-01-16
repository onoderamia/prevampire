# `prevampire`

![GitHub]()
[![Documentation Status]()]()
![PyPI]()

PREVAMPIRE is a package made to work in supplementary with the [VAMPIRE package](https://github.com/tengjuilin/vampire-analysis). This package contains methods that expedite the user's preparation for the VAMPIRE pipeline, and limits the amount of code interaction needed for someone new to python. 

The package was made to turn raw tif images of microglia into numpy arrays so that the vampire package could be applied succesfully. This package also applies and outputs skeletonization on the images after thresholding. 

The VAMPIRE package returns a dataframe containing characteristics of each microglia identified within the dataset and return average shape modes. 

Cell morphology is used as a support to show the effectivity of therapudics.   

## Installation

If Python is installed on your machine, type the following line into your command prompt to install via [PyPI]():

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

Below are a list of methods you want to apply. Take a look at the method comments in prevampire.py within the prevampire file for more information. 

 ```python

max_imgs, org_names = take_channel(raw_dir, print_image = 1)

threshall_dir = 'new/file/path' # new file
apply_and_save_all_thresholds(max_imgs, org_names, threshall_dir)

thresh_imgs, thresh_names = apply_threshold(max_imgs, org_names, print_image = 1)

skel_imgs, skel_names = skeletonize_images(thresh_imgs, thresh_names, print_image = 1)

skel_df = get_skel_df(skel_imgs, skel_name, show = 1)

```

Below are a list of supplementary methods you can use throughout the pipeline above. 

 ```python

save_tif(result_img, names, '/Users/miaonodera/Desktop/Extracirriculars/nance-lab/prevampire/prevampire/tests/data/denoisedtif')

save_npy(result_img, names, '/Users/miaonodera/Desktop/Extracirriculars/nance-lab/prevampire/prevampire/tests/data/denoisednpy')

load_tif_imgs()

load_npy_imgs()

display_img_side(thresh_img, skel_imgs, 2, 'thresh', 'skel')

save_df(skel_df, 'skel_df', '/Users/miaonodera/Desktop/Extracirriculars/nance-lab/prevampire/prevampire/tests/data/assertdata')

```



## References

