"""
checks for the installation of various third party packages
use python_virtualenvs\datamining
require python 3.x or higher

test data:
    (for PIL and Tesseract)
    test_pillow.png
"""

# check for numpy package
import numpy as np
a = np.arange(15).reshape(3,5)
print(a)

# check for pandas
import pandas as pd
print('Pandas version' + pd.__version__)

names = ['bob', 'jessica','mary','john','mel']
births = [968,155,77,578,973]
baby_data_set = list(zip(names,births))
print(baby_data_set)

df = pd.DataFrame(data = baby_data_set, columns =['Names','Births'])
print(df)

from pprint import pprint as pp
pp(df)

# check for scipy
from scipy import linalg
A = np.array([[1,2],[3,4]])
print(A)
A_inv = linalg.inv(A)
print(A_inv)

# check for Pillow(Python Imaging Library)
from PIL import Image
im = Image.open("test_pillow.png")
print("Image format = {}".format(im.format))
print("Image size = {}".format(im.size))
print("Image mode = {}".format(im.mode))

# check for tesseract
# NOTE: Following Failed!!
import pytesseract
try:
    print(pytesseract.image_to_string(im))
except:
    print("pytesseract check failed!!!")

# check for StringIO
try:
    from StringIO import StringIO
except(ImportError):
    print("Error importing StringIO. So importing io.StringIO")
    from io import StringIO

# check gnupg
import gnupg
try:
    gpg = gnupg.GPG()
except(RuntimeError) as e:
    print(str(e))
except:
    print("gnupg check failed!!!")

