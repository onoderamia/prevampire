import prevampire as pv
import numpy.testing as npt
import shutil
import os
import pandas as pd

from pandas.testing import assert_frame_equal

raw_img_file = 'data/rawimgtif/'
input_file = 'data/input/'
output_file = 'data/output/'

def _remove_all(directory):
    arr = os.listdir(directory)
    arr = [os.path.join(directory, x) for x in arr]
    for file in arr:
        os.remove(file)

def test_remove_files():
    shutil.copy(raw_img_file, input_file)
    arr = os.listdir(raw_img_file)
    arr = [x for x in arr if 'cor' in x]
    pv.remove_files(input_file, 'cor')
    check = os.listdir(input_file)
    npt.assert_equal(arr, check)

    _remove_all(input_file)


def test_move_files():
    shutil.copy(raw_img_file, input_file)
    arr = os.listdir(raw_img_file)
    arr1 = [x for x in arr if 'hipca' in x]
    arr2 = [x for x in arr if 'hipca' not in x]
    pv.move_files(input_file, output_file, 'hipca')
    check1 = os.listdir(output_file)
    check2 = os.listdir(input_file)
    npt.assert_equal(arr1, check1)
    npt.assert_equal(arr2, check2)

    _remove_all(input_file)
    _remove_all(output_file)


def test_take_channel():
    shutil.copy(raw_img_file, input_file)
    img, name = pv.take_channel(input_file)
    img = np.array(img)
    name = np.array(name)
    img_assert = np.load('data/assertdata/denoised_img_arr.npy')
    name_assert = np.load('data/assertdata/denoised_names.npy')
    npt.assert_equal(img, img_assert)
    npt.assert_equal(name, name_assert)
    _remove_all(input_file)

def test_save_npy():
    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')
    pv.save_npy(imgs, name, output_file)
    arr = os.listdir(output_file)
    npt.assert_equal(name, arr)
    _remove_all(output_file)

def test_save_tif():
    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')
    pv.save_tif(imgs, name, output_file)

    for i in range(len(name)):
        basename, extension = os.path.splitext(name[i])
        name[i] = basename + '.tif'

    arr = os.listdir(output_file)

    npt.assert_equal(name, arr)

    _remove_all(output_file)

def test_apply_and_save_all_thresholds():
    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')

    apply_and_save_all_thresholds(imgs, name, output_file)

    check = os.listdir(output_file)

    npt.assert_equal(len(check), 5)
    
    _remove_all(output_file)

def test_apply_threshold():
    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')
 
    seg1, name1 = pv.apply_threshold(imgs, name)

    seg2 = np.load('data/assertdata/threshli_img_arr.npy')
    name2 = np.load('data/assertdata/threshli_names.npy')

    npt.assert_equal(seg1, seg2)
    npt.assert_equal(name1, name2)


def test_skeletonize_images():
    imgs = np.load('data/assertdata/threshli_img_arr.npy')
    name = np.load('data/assertdata/threshli_names.npy')

    skel1, name1 = pv.skeletonize_images(imgs, name)

    skel2 = np.load('data/assertdata/threshli_img_arr.npy')
    name2 = np.load('data/assertdata/threshli_names.npy')

    npt.assert_equal(skel1, skel2)
    npt.assert_equal(name1, name2)
 

def test_load_npy_imgs():
    shutil.copy('data/denoisednpy', input_file)
    data, names = pv.load_npy_imgs(input_file)

    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')

    npt.assert_equal(data, imgs)
    npt.assert_equal(names, name)

    _remove_all(input_file)


def test_load_tif_imgs():
    shutil.copy('data/denoisedtif', input_file)
    data, names = pv.load_tif_imgs(input_file)

    imgs = np.load('data/assertdata/denoised_img_arr.npy')
    name = np.load('data/assertdata/denoised_names.npy')

    npt.assert_equal(data, imgs)
    npt.assert_equal(names, name)

    _remove_all(input_file)

def test_get_skel_df():
    imgs = np.load('data/assertdata/skel_img_arr.npy')
    name = np.load('data/assertdata/skel_names.npy')

    df1 = get_skel_df(imgs, name)

    df2 = pd.read_csv('data/assertdata/skel_df.csv')

    assert_frame_equal(df1, df1)



     







