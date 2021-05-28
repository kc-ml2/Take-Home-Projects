import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import *

### data import
traindata = pd.read_csv('mitbih_train.csv', header=None)
testdata = pd.read_csv('mitbih_test.csv',header=None)

### write baseline code for newbies
