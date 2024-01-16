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
>>> import prevampire as pv  # recommended import signature
```

 Below are a list of methods you want to apply. Take a look at the method comments in prevampire.py within the prevampire file for more information. 

 ```python
>>> file_dir = 'file/path'  # file path to .tif images
>>> result_img, names = take_channel(file_list, print_image = 1)  # take the iba, print_image (optional)
>>> result_img, names = take_channel(file_list, print_image = 1)  # take the iba, print_image (optional)

```





## References

