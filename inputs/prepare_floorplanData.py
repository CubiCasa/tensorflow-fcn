# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:50:47 2015

@author: teichman
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import time
import numpy as np
import scipy as scp
import scipy.misc
import sys
from random import shuffle



def make_val_split(data_folder, all_file, test_perc):
    """
    Splits the Images in train and test.
    Assumes a File all.txt in data_folder.
    """

    train_file = "train.txt"
    test_file = "val.txt"

    filename = os.path.join(data_folder, all_file)
    assert os.path.exists(filename), ("File not Found %s"
                                      % filename)

    files = [line for line in open(filename)]

    shuffle(files)

    train = files[:-test_num]
    test = files[-test_num:]

    train_file = os.path.join(data_folder, train_file)
    test_file = os.path.join(data_folder, test_file)

    with open(train_file, 'w') as file:
        for label in train:
            file.write(label)

    with open(test_file, 'w') as file:
        for label in test:
            file.write(label)


def main():

    data_dir = "/home/petteri/Dropbox/CubiCasa Team Folder/data/semanticSegmentation/semanticSegmentationLabels/source" # quick'n'dirty
    all_file = "all.txt"
    test_perc = 30


    make_val_split(data_dir, all_file, test_num)


if __name__ == '__main__':
    main()
