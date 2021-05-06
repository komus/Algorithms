#Check required packages
try:
    import numpy
except ImportError:
    print("Error with numpy")

try:
    import nltk
except ImportError:
    print("Error importing Nltk")

try:
    import urllib.request
except ImportError:
    print("urllib")


# #download required files
# url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
# urllib.request.urlretrieve(url, filename="../enron_mail_20150507.tar.gz") 

import os
import tarfile
#unzip the file
#os.chdir("/data")
tfile = tarfile.open(r"path_to_downloaded_file", "r:gz")
tfile.extractall(".")
